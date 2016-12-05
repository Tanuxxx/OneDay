from Application.app_dashboard import AppDashboard

CATEGORY_BOARD_PATH = '/Admin/Category'
CATEGORY_NAME_IN_APP_DROPBOX = 'Categories'


class CategoryDashboard(AppDashboard):
    def __init__(self, app):
        super().__init__(app)

    def get_category_board_path(self):
        return CATEGORY_BOARD_PATH

    def get_category_name_in_app_box(self):
        return CATEGORY_NAME_IN_APP_DROPBOX