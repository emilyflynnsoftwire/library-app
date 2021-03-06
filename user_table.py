from datetime import date, datetime

DATE_FORMAT = "%Y-%d-%m"

class ValidationError(Exception):
    pass


class GenUser():
    def __init__(self, db_data, validate=True):
        self.id = db_data["GenUserId"]
        self.first_name = db_data["firstName"]
        self.middle_names = db_data["middleNames"]
        self.last_name = db_data["lastName"]
        self.date_of_birth = db_data["dateOfBirth"]
        self.email_address = db_data["emailAddr"]
        self.phone_number_1_type = db_data["phoneNo1Type"]
        self.phone_number_1 = db_data["phoneNo1"]
        self.phone_number_2_type = db_data["phoneNo2Type"]
        self.phone_number_2 = db_data["phoneNo2"]
        self.address_line_1 = db_data["addrLine1"]
        self.address_line_2 = db_data["addrLine2"]
        self.town = db_data["townCity"]
        self.postcode = db_data["postcode"]
        self._cast_properties()
        if validate:
            self.validate()

    @classmethod
    def from_db(cls, db, id):
        db_data = db.execute("""
            SELECT GenUser.id as GenUserId, *
            FROM GenUser
            WHERE GenUser.id = ?
            """, (id,)).fetchone()
        return cls(db_data, validate=False)

    def update(self, form):
        for key, value in form.items():
            if hasattr(self, key):
                setattr(self, key, value)
        self._cast_properties()
        self.validate()

    def validate(self):
        if len(self.first_name) == 0:
            raise ValidationError("First name required")
        if len(self.last_name) == 0:
            raise ValidationError("last name required")
        if len(self.email_address) == 0:
            raise ValidationError("Email address required")
        if len(self.postcode) == 0:
            raise ValidationError("Postcode required")

    def save(self, db):
        db.execute("""
        UPDATE GenUser
        SET (firstName, middleNames, lastName, dateOfBirth, emailAddr,
            phoneNo1Type, phoneNo1, phoneNo2Type, phoneNo2, addrLine1,
            addrLine2, townCity, postcode)
            =
            (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        WHERE id = ?
        """, (self.first_name, self.middle_names, self.last_name,
            self.date_of_birth.strftime(DATE_FORMAT) if type(self.date_of_birth) == date else self.date_of_birth,
            self.email_address, self.phone_number_1_type, self.phone_number_1,
            self.phone_number_2_type, self.phone_number_2, self.address_line_1,
            self.address_line_2, self.town, self.postcode, self.id))

    def _cast_properties(self):
        self.id = int(self.id)
        if type(self.date_of_birth) == str:
            try:
                self.date_of_birth = datetime.strptime(self.date_of_birth, DATE_FORMAT).date()
            except ValueError:
                pass

        

class PublicUser(GenUser):

    def __init__(self, db_data, validate=True):
        self.card_number = db_data["cardNo"]
        self.reg_date = db_data["regDate"]
        super().__init__(db_data, validate=validate)

    @classmethod
    def from_db(cls, db, id):
        db_data = db.execute("""
            SELECT GenUser.id as GenUserId, *
            FROM GenUser 
            LEFT JOIN PublicUser
            ON GenUser.id = PublicUser.userId
            WHERE GenUser.id = ?
            """, (id,)).fetchone()
        return cls(db_data, validate=False)

    def validate(self):
        if not self.card_number >  0:
            raise ValidationError("Card number must be positive.")
        super().validate()

    def save(self, db):
        super().save(db)

    def _cast_properties(self):
        self.card_number = int(self.card_number)
        super()._cast_properties()