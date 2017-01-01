VIDEO_PLAYER_PATH = '/Admin/Video'
LOGGED_IN_USER_EMAIL_XPATH = '//header//div[@class="user col-xs-3 col-sm-3 text-right"]//div[@class="dropdown"]'
VIDEO_XPATH = '//div[@class="video-container"]/div[@id="vjs_video_3"]/video/source'
VIDEO_FILE_NAME = 'video.mp4'
VIDEO_PLAYER_PAGE_TITLE = 'Video Player - OneDay'

class VideoPlayer:
    def __init__(self, app):
        self.app = app

    def get_video_player_path(self):
        return VIDEO_PLAYER_PATH

    def get_logged_in_user_email(self):
        return self.app.driver.find_element_by_xpath(LOGGED_IN_USER_EMAIL_XPATH).text

    def get_video_src(self):
        return self.app.driver.find_element_by_xpath(VIDEO_XPATH).get_attribute('src')

    def get_video_file_name(self):
        return VIDEO_FILE_NAME

    def get_video_player_page_title(self):
        return VIDEO_PLAYER_PAGE_TITLE



