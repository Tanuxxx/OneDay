import os
#import pymssql

from selenium import webdriver

from OneDay.Community.community_dashboard import CommunityDashboard
from OneDay.Community.resident_landing import ResidentLanding
from OneDay.Community.video_player import VideoPlayer
from OneDay.Company.company_dashboard import CompanyDashboard
from OneDay.Login.session import Session
from OneDay.MyStory.my_story_dashboard import MyStoryDashboard
from OneDay.Story.story_dashboard import StoryDashboard

TEST_SERVER_URL = 'st.oneday.com'
PROD_SERVER_URL = 'oneday.com'
PROTOCOL = 'http'

FOOTER_TEXT_XPATH = '//footer//section[2]/p'
FOOTER_LINK_XPATH = '//footer//section[2]/p/a'

FOOTER_TEXT = 'For support, contact us at support@oneday.com'
FOOTER_LINK = 'mailto:support@oneday.com'


class Application:
    def __init__(self, server_type):
        self.driver = webdriver.Chrome(os.path.dirname(os.getcwd()) + '/Tools/chromedriver.exe')
        #self.driver.maximize_window()
        self.driver.implicitly_wait(3)

        if server_type is not None and server_type.lower().find('prod') >= 0:
            self.server_url = PROD_SERVER_URL
        else:
            self.server_url = TEST_SERVER_URL

        self.session = Session(self)
        self.my_story_board = MyStoryDashboard(self)
        self.company_board = CompanyDashboard(self)
        self.community_board = CommunityDashboard(self)
        self.resident_landing = ResidentLanding(self)
        self.video_player = VideoPlayer(self)
        self.story_board = StoryDashboard(self)

        #Create DB connection
        #
        # self.db_connection = pymssql.connect(server='onedayweb-test.cpiqjs9uzigz.us-west-2.rds.amazonaws.com',
        #                                      user='onedayusertest', password='1prOgrAmmIng!', database='OneDay')
        # self.db_cursor = self.db_connection.cursor()

    def destroy(self):
        #Close browser
        self.driver.close()

        #Close connection to the DB
        # self.db_cursor.close()
        # self.db_connection.close()

    def get_server_url(self):
        return self.server_url

    def get_server_cms_url(self):
        return self.add_protocol_to_url('cms.' + self.server_url)

    def add_protocol_to_url(self, url):
        return PROTOCOL + '://' + url

    def get_footer_text(self):
        return self.driver.find_element_by_xpath(FOOTER_TEXT_XPATH).text

    def get_footer_link(self):
        return self.driver.find_element_by_xpath(FOOTER_LINK_XPATH).get_attribute('href')

    def get_expected_footer_text(self):
        return FOOTER_TEXT

    def get_expected_footer_link(self):
        return FOOTER_LINK
