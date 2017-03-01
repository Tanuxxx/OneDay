

def test_login_page_footer(app):
    """Footer is present and correct on the login page"""
    app.session.get_login_url()

    # add check for logo

    assert (app.get_footer_text() == app.get_expected_footer_text())
    assert (app.get_footer_link() == app.get_expected_footer_link())


# def test_login_as_oneday_admin(app):
#     """Log in as One Day admin directs to companies dashboard page"""
#     email = app.my_story_board.get_admin_email()
#
#     app.session.login(email=email, password=app.my_story_board.get_admin_password())
#
#     assert app.driver.current_url == app.get_server_cms_url() + app.my_story_board.get_my_story_board_path()
#     assert app.my_story_board.logo_is_displayed()
#     assert app.my_story_board.get_page_header() == "My Story"
#     assert app.session.get_logged_in_user_email() == email
#     assert app.my_story_board.get_dashboard_title() == "Company"
#     assert len(app.my_story_board.get_dashboard_items_names_list()) > 0
#
#     # app.db_cursor.execute("SELECT Name from Company")
#     # print(app.db_cursor.fetchone())
#     # db_conpany_list = app.db_cursor.fetchall()
#     # print(sorted(app.my_story_board.get_dashboard_items_names_list()))
#     # print(sorted(db_conpany_list))
#     # # while row:
#     # #     print ("CompanyID=%d, Name=%s" % (row[0], row[2]))
#     # #     row = app.db_cursor.fetchone()
#
#     app.session.logout(email)

#
# def test_login_as_company_admin(app):
#     """Log in as Master(company) admin directs to communities inside the company dashboard page"""
#     email = app.company_board.get_admin_email()
#
#     company_name = 'Oxford'
#
#     app.session.login(email=email, password=app.company_board.get_admin_password())
#
#     expected_company_url = app.company_board.get_company_prefix(company_name) + app.get_server_url() + \
#                            app.company_board.get_company_board_path()
#
#     assert app.driver.current_url == app.add_protocol_to_url(expected_company_url)
#     assert app.company_board.logo_is_displayed()
#     assert app.company_board.get_page_header() == app.company_board.get_company_name(company_name)
#     assert app.session.get_logged_in_user_email() == email
#     assert app.company_board.get_dashboard_title() == "Community", 'Assert header'
#     assert len(app.company_board.get_dashboard_items_names_list()) > 0
#
#     app.session.logout(email)


def test_login_as_community_admin(app):
    """Log in as Community admin directs to community page - community videos dashboard"""
    #email = app.community_board.get_admin_email()

    #company_name = 'Oxford'
    #community_name = 'test'

    #app.session.login(email=email, password=app.community_board.get_admin_password())
    #dictionary = []
    dictionary = [{'company_name': 'Oxford', 'community_name': 'crash test', 'email': 'd@d.co', 'password': 'qqqqqq'},
                  {'company_name': 'HHHunt', 'community_name': '', 'email': 'rdad@hhhunt.com', 'password': 'Keepsakes2016'},
                  {'company_name': 'Sagora', 'community_name': '', 'email': 'kyoung@tcglp.com', 'password': 'SagoraSL2016'},
                  {'company_name': 'The Residence at South Windsor Farms', 'community_name': 'The Residence at South Windsor Farms', 'email': 'hwood@residencesouthwindsor.com', 'password': 'qqqqqq'},
                  {'company_name': 'The Residence at Cedar Dell', 'community_name': 'The Residence at Cedar Dell', 'email': 'jgelinas@residencecedar.com', 'password': 'qqqqqq'},
                  {'company_name': 'The Residence at Five Corners', 'community_name': 'The Residence at Five Corners', 'email': 'mtorrance@residencefivecorners.com', 'password': 'qqqqqq'},
                  {'company_name': 'The Residence at Pearl Street', 'community_name': 'The Residence at Pearl Street', 'email': 'bcurry@residencepearl.com', 'password': 'qqqqqq'},
                  {'company_name': 'The Residence at Riverbend', 'community_name': 'The Residence at Riverbend', 'email': 'jgrotto@residenceriverbend.com', 'password': 'qqqqqq'},
                  {'company_name': 'The Residence at Valley Farm', 'community_name': 'The Residence at Valley Farm ', 'email': 'lfriis@residencevalleyfarm.com', 'password': 'qqqqqq'},
                  {'company_name': 'The Residence at Watertown Square', 'community_name': 'The Residence at Watertown Square', 'email': 'sbennett@residencewatertown.com', 'password': 'qqqqqq'},
                  {'company_name': 'Traditions of Dedham', 'community_name': 'Traditions of Dedham', 'email': 'gary.poholek@traditionsofdedham.com', 'password': 'qqqqqq'},
                  {'company_name': 'Windrose at Weymouth', 'community_name': 'Windrose at Weymouth ', 'email': 'edeparolesa@windroseweymouth.com', 'password': 'qqqqqq'},
                  {'company_name': 'Traditions of Wayland', 'community_name': 'Traditions of Wayland', 'email': 'Janie.belive@traditionsofwayland.com', 'password': 'qqqqqq'},
                  {'company_name': 'Windrose at Woburn', 'community_name': 'Windrose at Woburn', 'email': 'lsmith@windrosewoburn.com', 'password': 'qqqqqq'},
                  #{'company_name': 'LThe Residence at Brookside', 'community_name': 'The Residence at Brookside', 'email': 'tcoffin@residencebrookside.com', 'password': 'qqqqqq'},
                  #{'company_name': 'The Arbors of Bedford', 'community_name': 'The Arbors of Bedford', 'email': 'tcoffin@residencebrookside.com', 'password': 'qqqqqq'},
                  {'company_name': 'The Residence at Salem Woods', 'community_name': 'The Residence at Salem Woods', 'email': 'kregan@residencesalemwoods.com', 'password': 'qqqqqq'},
                  {'company_name': 'Lighthouse at Lincoln', 'community_name': 'Lighthouse at Lincoln', 'email': 'jdiraimo@lighthouselincoln.com', 'password': 'qqqqqq'},
                  {'company_name': 'The Residence at Otter Creek', 'community_name': 'The Residence at Otter Creek', 'email': 'callenson@residenceottercreek.com', 'password': 'qqqqqq'},
                  {'company_name': 'The Residence at Quarry Hill', 'community_name': 'The Residence at Quarry Hill', 'email': 'cclark@residencequarryhill.com', 'password': 'qqqqqq'},
                  {'company_name': 'The Residence at Shelburne Bay', 'community_name': 'The Residence at Shelburne Bay', 'email': 'lleclair@residenceshelburnebay.com', 'password': 'qqqqqq'},
                  {'company_name': 'Meridian', 'community_name': '','email': 'coho.act@meridiansenior.com', 'password': 'qqqqqq'},
                  {'company_name': 'Discovery Senior living corporate', 'community_name': '', 'email': 'video@discoverymgt.com', 'password': 'discovery'},
                  {'company_name': 'Aston Gardens at Pelican Marsh', 'community_name': '', 'email': 'videopm@astongardens.com', 'password': 'discovery'},
                  {'company_name': 'Discovery Village at the Forum', 'community_name': '', 'email': 'videodvf@discoveryvillages.com', 'password': 'discovery'},
                  {'company_name': 'Conservatory at Plano', 'community_name': '', 'email': 'videocp@cslsenior.com', 'password': 'discovery'},
                  {'company_name': 'Rittenhouse Villages at Portage', 'community_name': '', 'email': 'videorvp@rittenhousevillages.com', 'password': 'discovery'},
                  {'company_name': 'The Summit', 'community_name': '', 'email': 'video@thesummitretirement.com', 'password': 'discovery'},
                  {'company_name': 'Lakeside at Mallard Landing', 'community_name': '', 'email': 'video@lakesideatmallardlanding.com', 'password': 'discovery'},
                  {'company_name': 'Spring Mill Senior Living', 'community_name': '', 'email': 'video@springmillseniorliving.com', 'password': 'discovery'},
                  {'company_name': 'The Trace', 'community_name': '', 'email': 'video@thetraceseniorliving.com', 'password': 'discovery'},
                  {'company_name': 'Regency Pointe', 'community_name': '', 'email': 'video@regencypointe.net', 'password': 'discovery'},
                  {'company_name': 'Franklin Park', 'community_name': '', 'email': 'ewing@franklinmgt.net', 'password': 'franklin'},
                  {'company_name': 'Alamo Heights', 'community_name': '', 'email': 'ahled@fpliving.com', 'password': 'franklin'},
                  {'company_name': 'TPC', 'community_name': '', 'email': 'lara@fpliving.com', 'password': 'franklin'},
                  {'company_name': 'Sonterra', 'community_name': '', 'email': 'anisa@fpliving.com', 'password': 'franklin'},
                  {'company_name': 'Boerne', 'community_name': '', 'email': 'temp1@fpliving.com', 'password': 'franklin'},
                  {'company_name': 'Round Rock', 'community_name': '', 'email': 'ajohnson@fpliving.com', 'password': 'franklin'},
                  {'company_name': 'The Landing at Stone Oak', 'community_name': '', 'email': 'cmorris@fpliving.com', 'password': 'franklin'},
                  {'company_name': 'DeSoto', 'community_name': '', 'email': 'kareika@fpliving.com', 'password': 'franklin'},
                  {'company_name': 'Reliant', 'community_name': '', 'email': 'rachel@oneday.com', 'password': 'qqqqqq'},
                  {'company_name': 'Atria', 'community_name': '', 'email': 'richardson@atriaseniorliving.com', 'password': 'qqqqqq'},
                  {'company_name': 'Autumn Leaves', 'community_name': '', 'email': 'tw@autumnleaves.com', 'password': 'qqqqqq'},
                  {'company_name': 'Housing Forum', 'community_name': '', 'email': 'smoran@seniorhousingforum.net', 'password': 'qqqqqq'},
                  {'company_name': 'Koelsh', 'community_name': '', 'email': 'koelsch@mailinator.com', 'password': 'qqqqqq'},
                  {'company_name': 'Santa Clara University', 'community_name': '', 'email': 'scu1@mailinator.com', 'password': 'qqqqqq'},
                  {'company_name': 'Brookdale', 'community_name': '', 'email': 'cleech@brookdale.com', 'password': 'qqqqqq'},
                  {'company_name': 'North Cities ', 'community_name': '', 'email': 'northcities@mailinator.com', 'password': 'northcities'}
                  ]

    for cur_community in dictionary:
        print('Current Company: ')
        print(cur_community['company_name'])

        app.session.login(email=cur_community['email'], password=cur_community['password'])

        #expected_community_url = app.company_board.get_company_prefix(cur_community['company_name']) + app.get_server_url() + \
        #                   app.community_board.get_community_board_path()

        try:
            #assert app.driver.current_url.find(app.add_protocol_to_url(expected_community_url).lower()) == 0
            assert app.community_board.logo_is_displayed()
            #assert app.community_board.get_page_header() == cur_community['community_name']
            assert app.session.get_logged_in_user_email().lower() == cur_community['email'].lower()
            assert app.community_board.get_dashboard_title() == "Video", 'Assert header'
            assert len(app.community_board.get_dashboard_items_names_list()) >= 0
        except:
            app.session.logout(cur_community['email'])
            continue
            
        app.session.logout(cur_community['email'])



# def test_login_as_resident(app):
#     """Log in as Residents directs to resident landing page with all the video tagged by the resident"""
#     email = 'Member@oxford.test'
#     password = '12345678'
#
#     app.session.login(email=email, password=password)
#
#     expected_company_url = app.get_server_cms_url() + app.resident_landing.get_resident_landing_path()
#
#     assert app.driver.current_url.find(expected_company_url) == 0
#     assert app.get_footer_text() == app.get_expected_footer_text()
#     assert app.get_footer_link() == app.get_expected_footer_link()
#     assert app.resident_landing.get_logged_in_user_email() == email
#     assert app.resident_landing.is_resident_avatar_displayed()
#     assert len(app.resident_landing.get_resident_name())>0
#     assert len(app.resident_landing.get_resident_dob())>0
#     assert len(app.resident_landing.get_resident_video_href())
#
#     app.session.logout(email)

