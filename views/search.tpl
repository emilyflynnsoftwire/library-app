% rebase('base.tpl', searchpage=True, dispsignin=True, buttontext=buttontext, signout=signout)

        <main role="main">

            <div class="jumbotron">
                <div class="container">
                    <h1 class="display-4">Search</h1>
                </div>
            </div>

            <div class="white-bg" style="height: 100%;">

            <div class="container">
                <form>
                    <div class="input-group mb-3">
                        <div class="input-group-prepend">
                            <select class="selectpicker" data-style="btn-outline-info" name="field">
                                <option>Title</option>
                                <option>Author</option>
                            </select>
                        </div>
                        <input type="text" name="searchdata" class="form-control" aria-label="Text input with dropdown button">
                        <div class="input-group-append">
                            <button class="btn btn-info" type="submit">&nbsp;Go&nbsp;</button>
                        </div>
                    </div>
                </form>

                % if 'results' in globals():
                    <hr class="section-divider">
                    
                    <div class="list-group" style="padding-bottom: 30px;">
                    % for item in results:
                        <a href="/book/{{item.id}}" class="list-group-item list-group-item-action flex-column align-items-start">
                            <div class="d-flex w-100 justify-content-between">
                                <h5 class="mb-1">{{ item.getBookDetail('bookName') }}</h5>
                                % if item.getBookDetail('url'):
                                    <small class="text-muted text-right">Online Resource<br><i class="fas fa-desktop"></i></small>
                                % end
                            </div>
                            <p class="mb-1">{{ item.authorString }}</p>
                            <small class="text-muted">To come: publisher, location, year published</small>
                        </a>
                    % end

                % end
                </div>

            </div> <!-- /container -->

            </div>

        </main>