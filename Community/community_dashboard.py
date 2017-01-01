from OneDay.Company.company_dashboard import CompanyDashboard

COMMUNITY_BOARD_PATH = '/Admin/Video/Community/'
ADMIN_EMAIL = 'CommunityAdmin@oxford.test'
ADMIN_PASSWORD = '12345678'
VIDEO_LIST_XPATH = '//tbody//td[@data-title="Video"]//div/p[@class="secondary color"]/a'


class CommunityDashboard(CompanyDashboard):
    def __init__(self, app):
        super().__init__(app)
        self.admin_email = ADMIN_EMAIL
        self.admin_password = ADMIN_PASSWORD

    def get_community_board_path(self):
        return COMMUNITY_BOARD_PATH

    def get_video_list_href(self):
        # video_list = self.app.driver.find_elements_by_xpath(VIDEO_LIST_XPATH)
        # video_list_href = []
        #
        # while video_list:
        #     video_list_href.append(video_list.pop().get_attribute('href'))
        # return video_list_href
        return self.app.driver.find_elements_by_xpath(VIDEO_LIST_XPATH)
