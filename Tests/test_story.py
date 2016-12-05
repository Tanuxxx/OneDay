

def test_story_dashboard(app):
    """Check opening story page from communities list page as App->Stories"""
    email = app.company_board.get_admin_email()

    company_name = 'Oxford'

    app.session.login(email=email, password=app.company_board.get_admin_password())

    app.story_board.go_to_app_item(app.story_board.get_story_name_in_app_box())

    expected_company_url = app.company_board.get_company_prefix(company_name) + app.get_server_url() + \
                           app.story_board.get_story_board_path()

    assert app.driver.current_url == app.add_protocol_to_url(expected_company_url), 'Assert page URL'
    assert app.story_board.logo_is_displayed(), 'Assert logo is displayed'
    assert app.story_board.get_page_header() == "Stories", 'Assert page header'
    assert app.session.get_logged_in_user_email() == email, 'Assert logged in user email'
    assert app.story_board.get_dashboard_title() == "Story", 'Assert header'
    assert len(app.story_board.get_dashboard_items_names_list()) > 0, 'Assert list of stories is not empty'

