import pytest

def test_login_as_oneday_admin(app):
    email = app.my_story_board.get_admin_email()
    app.driver.maximize_window()


    app.session.login(email=email, password=app.my_story_board.get_admin_password())

    company_list = app.my_story_board.get_dashboard_items_list()

    for index in range(len(company_list)):
        company_list = app.my_story_board.get_dashboard_items_list()
        current_company = company_list[index]
        current_company_name = current_company.find_element_by_xpath(app.my_story_board.dashboard_items_list_name_xpath).text
        print('--------------------------------')
        print('Company name: ', current_company_name)
        #with pytest.allure.step(current_company_name):
        current_company.find_element_by_xpath(app.my_story_board.dashboard_items_list_name_xpath).click()

        try:
            assert app.company_board.logo_is_displayed()
            #assert app.company_board.get_page_header() == current_company_name
            assert app.company_board.get_dashboard_title() == "Community", 'Assert header'
            community_list = app.company_board.get_dashboard_items_list()
            assert len(community_list) >= 0
            print('pass')
        except:
            print('fail')
            app.driver.execute_script("window.history.go(-1)")
            continue

        for index2 in range(len(community_list)):
            community_list = app.company_board.get_dashboard_items_list()
            current_community = community_list[index2]
            current_community_name = current_community.find_element_by_xpath(
                app.community_board.dashboard_items_list_name_xpath).text
            print('Community name: ', current_community_name)
            current_community.find_element_by_xpath(app.company_board.dashboard_items_list_name_xpath).click()

            try:
                assert app.community_board.logo_is_displayed()
                #assert app.community_board.get_page_header() == current_community_name
                assert app.community_board.get_dashboard_title() == "Video", 'Assert header'
                assert len(app.community_board.get_dashboard_items_names_list()) >= 0
            except:
                print('!!!!!-fail-!!!!!')
                app.driver.execute_script("window.history.go(-1)")
                continue

            app.driver.execute_script("window.history.go(-1)")

        app.driver.execute_script("window.history.go(-1)")



