from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen

class MainScreen(Screen):

    def SpotifyChangeScreen(self,instance):
        pass

    def NetflixNextScreen(self, instance):
        pass

class NetflixNewDataScreen(Screen):
    pass

class SpotifyNewDataScreen(Screen):
    pass

class NetflixLoadingScreen(Screen):
    pass

class NetflixDataAdapter():
    pass

class NetflixUpdateData():
    pass

class TMBDAApi():
    pass

class setUp(App):
    def build(self):
        Main_Screen = MainScreen(name='Main_Screen')
        Netflix_New_Data_Screen = NetflixNewDataScreen(name='Netflix_New_Data_Screen')
        Spotify_New_Data_Screen = SpotifyNewDataScreen(name='Spotify_New_Data_Screen')
        Netflix_Loading_Screen = NetflixLoadingScreen(name='Netflix_Loading_Screen')

        screen_manager = ScreenManager()
        screen_manager.add_widget(Main_Screen)
        screen_manager.add_widget(Netflix_New_Data_Screen)
        screen_manager.add_widget(Spotify_New_Data_Screen)
        screen_manager.add_widget(Netflix_Loading_Screen)

        return screen_manager

