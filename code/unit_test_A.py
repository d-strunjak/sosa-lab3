from math import nan
import math
import unittest

from dodatak_A import OperationsManager

class TestOperationsManager(unittest.TestCase):

    def test_regular_divison(self):
        o_m = OperationsManager(1, 2)
        res = o_m.perform_division()
        self.assertEqual(res, 1/2, f"Regular divison not successful, {res} != {1/2} !")
    
    def test_divison_numerator_zero(self):
        o_m = OperationsManager(0, 2)
        res = o_m.perform_division()
        self.assertEqual(res, 0, f"Divison with numerator 0 not successful, {res} != 0 !")
    
    def test_divison_denominator_zero(self):
        o_m = OperationsManager(1, 0)
        res = o_m.perform_division()
        self.assertTrue(math.isnan(res), f"Divison with denominator 0 not successful, {res} != NaN !")

    def test_divison_numerator_denominator_zero(self):
        o_m = OperationsManager(0, 0)
        res = o_m.perform_division()
        self.assertTrue(math.isnan(res), f"Divison with numberator and denominator both equal 0 not successful, {res} != NaN !")
        
if __name__ == '__main__':
    unittest.main()