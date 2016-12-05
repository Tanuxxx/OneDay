from Application.app_dashboard import AppDashboard

MOMENT_BOARD_PATH = '/Admin/Moment'
MOMENT_NAME_IN_APP_DROPBOX = 'Moments'


class MomentDashboard(AppDashboard):
    def __init__(self, app):
        super().__init__(app)

    def get_moment_board_path(self):
        return MOMENT_BOARD_PATH

    def get_moment_name_in_app_box(self):
        return MOMENT_NAME_IN_APP_DROPBOX