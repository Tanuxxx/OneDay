from Application.app_dashboard import AppDashboard

STORY_BOARD_PATH = '/Admin/Story'
STORY_NAME_IN_APP_DROPBOX = 'Stories'


class StoryDashboard(AppDashboard):
    def __init__(self, app):
        super().__init__(app)

    def get_story_board_path(self):
        return STORY_BOARD_PATH

    def get_story_name_in_app_box(self):
        return STORY_NAME_IN_APP_DROPBOX