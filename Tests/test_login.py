

def test_login_page_footer(app):
    """Footer is present and correct on the login page"""
    app.session.get_login_url()

    # add check for logo

    assert (app.get_footer_text() == app.get_expected_footer_text())
    assert (app.get_footer_link() == app.get_expected_footer_link())


def test_login_as_oneday_admin(app):
    """Log in as One Day admin directs to companies dashboard page"""
    email = app.my_story_board.get_admin_email()

    app.session.login(email=email, password=app.my_story_board.get_admin_password())

    assert(app.driver.current_url == app.get_server_cms_url() + app.my_story_board.get_my_story_board_path())
    assert(app.my_story_board.logo_is_displayed())
    assert(app.my_story_board.get_page_header() == "My Story")
    assert(app.session.get_logged_in_user_email() == email)
    assert(app.my_story_board.get_dashboard_title() == "Company")
    assert(len(app.my_story_board.get_dashboard_items_names_list()) > 0)

    # app.db_cursor.execute("SELECT Name from Company")
    # print(app.db_cursor.fetchone())
    # db_conpany_list = app.db_cursor.fetchall()
    # print(sorted(app.my_story_board.get_dashboard_items_names_list()))
    # print(sorted(db_conpany_list))
    # # while row:
    # #     print ("CompanyID=%d, Name=%s" % (row[0], row[2]))
    # #     row = app.db_cursor.fetchone()

    app.session.logout(email)


def test_login_as_company_admin(app):
    """Log in as Master(company) admin directs to communities inside the company dashboard page"""
    email = app.company_board.get_admin_email()

    company_name = 'Oxford'

    app.session.login(email=email, password=app.company_board.get_admin_password())

    expected_company_url = app.company_board.get_company_prefix(company_name) + app.get_server_url() + \
                           app.company_board.get_company_board_path()

    assert(app.driver.current_url == app.add_protocol_to_url(expected_company_url))
    assert(app.company_board.logo_is_displayed())
    assert(app.company_board.get_page_header() == app.company_board.get_company_name(company_name))
    assert(app.session.get_logged_in_user_email() == email)
    assert app.company_board.get_dashboard_title() == "Community", 'Assert header'
    assert(len(app.company_board.get_dashboard_items_names_list()) > 0)

    app.session.logout(email)


def test_login_as_community_admin(app):
    """Log in as Community admin directs to community page - community videos dashboard"""
    email = app.community_board.get_admin_email()

    company_name = 'Oxford'
    community_name = 'test'

    app.session.login(email=email, password=app.community_board.get_admin_password())

    expected_community_url = app.company_board.get_company_prefix(company_name) + app.get_server_url() + \
                           app.community_board.get_community_board_path()

    assert(app.driver.current_url.find(app.add_protocol_to_url(expected_community_url).lower()) == 0)
    assert(app.community_board.logo_is_displayed())
    assert(app.community_board.get_page_header() == community_name)
    assert(app.session.get_logged_in_user_email() == email)
    assert app.community_board.get_dashboard_title() == "Video", 'Assert header'
    assert(len(app.community_board.get_dashboard_items_names_list()) > 0)

    app.session.logout(email)


def test_login_as_resident(app):
    """Log in as Residents directs to resident landing page with all the video tagged by the resident"""
    email = 'Member@oxford.test'
    password = '12345678'

    app.session.login(email=email, password=password)

    expected_company_url = app.get_server_cms_url() + app.resident_landing.get_resident_landing_path()

    assert app.driver.current_url.find(expected_company_url) == 0
    assert (app.get_footer_text() == app.get_expected_footer_text())
    assert (app.get_footer_link() == app.get_expected_footer_link())
    assert (app.resident_landing.get_logged_in_user_email() == email)
    assert (app.resident_landing.is_resident_avatar_displayed())
    assert (len(app.resident_landing.get_resident_name())>0)
    assert (len(app.resident_landing.get_resident_dob())>0)
    assert (len(app.resident_landing.get_resident_video_href()))

    app.session.logout(email)

