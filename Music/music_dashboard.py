from Application.app_dashboard import AppDashboard

MUSIC_BOARD_PATH = '/Admin/AudioFile'
MUSIC_NAME_IN_APP_DROPBOX = 'Music'


class MusicDashboard(AppDashboard):
    def __init__(self, app):
        super().__init__(app)

    def get_music_board_path(self):
        return MUSIC_BOARD_PATH

    def get_music_name_in_app_box(self):
        return MUSIC_NAME_IN_APP_DROPBOX