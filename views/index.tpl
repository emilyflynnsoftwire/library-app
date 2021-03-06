% rebase('base.tpl', index_page=True, disp_signin=True, btn_text=signin_status.btn_text, is_signed_in=signin_status.is_signed_in)

        <main role="main">

            <div class="jumbotron index" id="fading-images">
                <div class="container">
                    <h1 class="display-4" id="main-header">Welcome to the Softwire Library website</h1>
                    <p><a class="btn btn-outline-info btn-info-white" href="/account" role="button">Go to my account &raquo;</a></p>
                </div>
            </div>

            <div class="white-bg">

            <div class="container">
                <h2 class="display-4 small-display">Quick search all books</h2>
                <form action="/search">
                    <div class="input-group mb-3">
                        <div class="input-group-prepend">
                            <select class="selectpicker" data-style="btn-outline-info" name="field">
                                <option id="Title">Title</option>
                                <option id="Author">Author</option>
                            </select>
                        </div>
                        <input type="text" name="searchdata" class="form-control" aria-label="Text input with dropdown button">
                        <div class="input-group-append">
                            <button class="btn btn-info" type="submit">&nbsp;Go&nbsp;</button>
                        </div>
                    </div>
                </form>

                <hr class="section-divider">

                <h2 class="display-4 small-display">Meet the team</h2>
                <div class="news-slider" style="margin-bottom: 50px">
                    <div class="slide"><img src="http://place-puppy.com/200x200"></div>
                    <div class="slide"><img src="http://place-puppy.com/200x200"></div>
                    <div class="slide"><img src="http://place-puppy.com/200x200"></div>
                    <div class="slide"><img src="http://place-puppy.com/200x200"></div>
                    <div class="slide"><img src="http://place-puppy.com/200x200"></div>
                    <div class="slide"><img src="http://place-puppy.com/200x200"></div>
                </div>

            </div> <!-- /container -->

            % include('footer.tpl')

            </div>

        </main>