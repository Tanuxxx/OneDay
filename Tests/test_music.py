

def test_music_dashboard(app):
    """Check opening music page from communities list page as App->Stories"""
    email = app.company_board.get_admin_email()

    company_name = 'Oxford'

    app.session.login(email=email, password=app.company_board.get_admin_password())

    app.music_board.go_to_app_item(app.music_board.get_music_name_in_app_box())

    expected_company_url = app.company_board.get_company_prefix(company_name) + app.get_server_url() + \
                           app.music_board.get_music_board_path()

    assert app.driver.current_url == app.add_protocol_to_url(expected_company_url), 'Assert page URL'
    assert app.music_board.logo_is_displayed(), 'Assert logo is displayed'
    assert app.music_board.get_page_header() == "Music", 'Assert page header'
    assert app.session.get_logged_in_user_email() == email, 'Assert logged in user email'
    assert app.music_board.get_dashboard_title() == "Music", 'Assert header'
    assert len(app.music_board.get_dashboard_items_names_list()) > 0, 'Assert list of music is not empty'