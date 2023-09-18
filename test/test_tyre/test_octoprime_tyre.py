import unittest
import sys     
sys.path.append('C:\\Users\\fahee\\Desktop\\Programming\\Virtual Internship\\lyft\\forage-lyft-task-3-model-answer-main\\tyres')
from octoprime_tyre import OctoprimeTyre

class TestOctoprimeTyre(unittest.TestCase):

    def test_needs_service_false(self):
        tyre_life = [0.5, 0.5, 0.9, 0.5]
        tyre = OctoprimeTyre(tyre_life)
        self.assertFalse(tyre.needs_service())

    def test_needs_service_true(self):
        tyre_life = [0.8, 0.8, 0.8, 0.8]
        tyre = OctoprimeTyre(tyre_life)
        self.assertTrue(tyre.needs_service())


if __name__ == "__main__":
    unittest.main()