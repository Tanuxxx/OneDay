from OneDay.Application.dashboard import Dashboard

STORY_BOARD_PATH = '/Admin/Story'


class StoryDashboard(Dashboard):
    def __init__(self, app):
        super().__init__(app)

    def get_story_board_path(self):
        return STORY_BOARD_PATH