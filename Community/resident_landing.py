RESIDENT_LANDING_PATH = '/Users'
RESIDENT_AVATAR_ID = 'avatar'
RESIDENT_NAME_XPATH = '//div[@class="profile"]/div/h1'
RESIDENT_DOB_XPATH = '//div[@class="profile"]/div/time'
RESIDENT_VIDEO_XPATH = '//div[@class="video col-sm-6 col-md-4 ng-scope"]/a'
LOGGED_IN_USER_EMAIL_XPATH = '//header//div[@class="user col-xs-3 col-sm-3 text-right"]//div[@class="dropdown"]'


class ResidentLanding:
    def __init__(self, app):
        self.app = app

    def get_resident_landing_path(self):
        return RESIDENT_LANDING_PATH

    def is_resident_avatar_displayed(self):
        return self.app.driver.find_element_by_id(RESIDENT_AVATAR_ID).is_displayed()

    def get_resident_name(self):
        return self.app.driver.find_element_by_xpath(RESIDENT_NAME_XPATH).text

    def get_resident_dob(self):
        return self.app.driver.find_element_by_xpath(RESIDENT_DOB_XPATH).text

    def get_resident_video_href(self):
        resident_video_list = self.app.driver.find_elements_by_xpath(RESIDENT_VIDEO_XPATH)
        resident_video_list_href = []

        while resident_video_list:
            resident_video_list_href.append(resident_video_list.pop().get_attribute('href'))
        return resident_video_list_href

    def get_logged_in_user_email(self):
        return self.app.driver.find_element_by_xpath(LOGGED_IN_USER_EMAIL_XPATH).text

