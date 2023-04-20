import unittest
import pandas as pd
from app import setUp
import time

class LoadingisFinished(unittest.TestCase):
    app = setUp()
    app.screen_manager = app.build()

    def testisFinished(self):
        start_time = time.time()
        self.netflix_loading = self.app.screen_manager.get_screen('Netflix_Loading_Screen')
        self.netflix_loading.startUpdatingData(None)
        if self.netflix_loading.finishedLoading == 1:
            end_time = time.time()
        else:
            end_time = time.time()*20
        duration = end_time - start_time
        self.assertLess(duration,240)

class UpdateFileisvalid(unittest.TestCase):

    app = setUp()
    app.screen_manager = app.build()

    def testUpdatevalid(self):
        self.netflix_loading = self.app.screen_manager.get_screen('Netflix_Loading_Screen')
        self.netflix_loading.startUpdatingData(None)
        self.file = self.netflix_loading.update
        self.testfile = pd.read_csv('./data_with_actress.csv')
        if self.testfile.equals(self.file): self.assertEqual(1,1)
        else: self.assertEqual(0,1)

class GoToNetflixMainScreen():
    app = setUp()
    app.screen_manager = app.build()

    def test(self):
        self.netflix_loading = self.app.screen_manager.get_screen('Netflix_Loading_Screen')
        self.netflix_loading.startUpdatingData(None)
        self.app.screen_manager.get_screen('Main_Screen').NetflixMainScreen(None)
        current_screen = self.app.screen_manager.current
        test1,test2 = 0,0
        if self.netflix_loading.finishedLoading == 1: test1 = 1
        if current_screen == 'Netflix_Main_Screen': test2 = 1
        self.assertEqual(test1,test2)
