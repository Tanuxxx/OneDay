

def test_theme_dashboard(app):
    """Check opening theme page from communities list page as App->Stories"""
    email = app.company_board.get_admin_email()

    company_name = 'Oxford'

    app.session.login(email=email, password=app.company_board.get_admin_password())

    app.theme_board.go_to_app_item(app.theme_board.get_theme_name_in_app_box())

    expected_company_url = app.company_board.get_company_prefix(company_name) + app.get_server_url() + \
                           app.theme_board.get_theme_board_path()

    assert app.driver.current_url == app.add_protocol_to_url(expected_company_url), 'Assert page URL'
    assert app.theme_board.logo_is_displayed(), 'Assert logo is displayed'
    assert app.theme_board.get_page_header() == "Themes", 'Assert page header'
    assert app.session.get_logged_in_user_email() == email, 'Assert logged in user email'
    assert app.theme_board.get_dashboard_title() == "Theme", 'Assert header'
    assert len(app.theme_board.get_dashboard_items_names_list()) > 0, 'Assert list of themes is not empty'
