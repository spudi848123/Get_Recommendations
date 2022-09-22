import sys, os
import unittest
# Adding src folder to the system path
SRC = os.path.join(os.getcwd(),"src")
sys.path.insert(0,SRC)
from field_recommend import *

FRINS = FieldRecommend("mock_rec.csv")
FRFIELDNAMES = FRINS.get_fieldnames()
Header1_values = ["value11 testvalue", "value12 testvalue", "value13 testvalue"]
Header2_values = ["value21 testvalue", "value22 testvalue", "value23 testvalue"]

class Testcsv(unittest.TestCase):

    def test_read_header1(self):
        self.assertEqual(FRINS.get_recommendations(FRFIELDNAMES[0], "testvalue"), Header1_values, "Should be [value11 testvalue, value12 testvalue, value13 testvalue]")

    def test_read_header2(self):
        self.assertEqual(FRINS.get_recommendations(FRFIELDNAMES[1], "testvalue"), Header2_values, "Should be [value21 testvalue, value22 testvalue, value23 testvalue]")

if __name__ == '__main__':
    unittest.main()