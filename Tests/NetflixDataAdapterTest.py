import unittest
import pandas as pd
from app import NetflixDataAdapter

class IsAdaptedWell(unittest.TestCase):

    def test(self):
        Ad = NetflixDataAdapter()
        self.data = './UserFile.csv'
        Ad.data = self.data
        Ad.remakeFile()
        self.filelink = Ad.csvFile
        self.testFile = pd.read_csv('./adapted_data.csv')
        with open(self.filelink, 'r') as f1:
            with open(self.testFile, 'r') as f2:
                for line1, line2 in zip(f1, f2):
                    self.assertEqual(line1, line2)

