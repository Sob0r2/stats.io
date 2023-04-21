import unittest
import pandas as pd
from app import TMBDAApi


class MovieDataUpdate(unittest.TestCase):

    def test(self):
        TMBD = TMBDAApi()
        self.testdata = pd.read_csv('./adapted_data.csv')
        TMBD.dataArray = self.testdata
        TMBD.getMovieData()
        self.data = TMBD.dataArray
        self.testdata = pd.read_csv('./Small_File_Test.csv')
        if self.testdata.equals(self.data): self.assertEqual(1,1)
        else: self.assertEqual(1,0)

class MovieGenres(unittest.TestCase):

    def test(self):
        TMBD = TMBDAApi()
        self.testdata = pd.read_csv('./Small_File_Test.csv')
        TMBD.dataArray = self.testdata
        TMBD.getGenres()
        self.data = TMBD.dataArray
        self.testdata = pd.read_csv('./data_with_genres.csv')
        if self.testdata.equals(self.data): self.assertEqual(1,1)
        else: self.assertEqual(1,0)

class MovieActors(unittest.TestCase):

    def test(self):
        TMBD = TMBDAApi()
        self.testdata = pd.read_csv('./data_with_genres.csv')
        TMBD.dataArray = self.testdata
        TMBD.getActors()
        self.data = TMBD.dataArray
        self.testdata = pd.read_csv('./data_with_actress.csv')
        if self.testdata.equals(self.data): self.assertEqual(1,1)
        else: self.assertEqual(1,0)
