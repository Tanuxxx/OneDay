from OneDay.Application.dashboard import Dashboard

MY_STORY_BOARD_PATH = '/Admin/Company'
ADMIN_EMAIL = 'jdineshk@gmail.com'
ADMIN_PASSWORD = 'brookdale2016'


class MyStoryDashboard(Dashboard):
    def __init__(self, app):
        super().__init__(app)
        self.admin_email = ADMIN_EMAIL
        self.admin_password = ADMIN_PASSWORD

    def get_my_story_board_path(self):
        return MY_STORY_BOARD_PATH



