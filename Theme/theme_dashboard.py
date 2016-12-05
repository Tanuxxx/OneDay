from Application.app_dashboard import AppDashboard

THEME_BOARD_PATH = '/Admin/Theme'
THEME_NAME_IN_APP_DROPBOX = 'Themes'


class ThemeDashboard(AppDashboard):
    def __init__(self, app):
        super().__init__(app)

    def get_theme_board_path(self):
        return THEME_BOARD_PATH

    def get_theme_name_in_app_box(self):
        return THEME_NAME_IN_APP_DROPBOX