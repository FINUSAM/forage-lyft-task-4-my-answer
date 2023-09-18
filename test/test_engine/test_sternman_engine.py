import unittest

import sys     
sys.path.append('C:\\Users\\fahee\\Desktop\\Programming\\Virtual Internship\\lyft\\forage-lyft-task-3-model-answer-main\\engine')

from sternman_engine import SternmanEngine


class TestSternmanEngine(unittest.TestCase):
    def test_needs_service_true(self):
        warning_light_is_on = True
        engine = SternmanEngine(warning_light_is_on)
        self.assertTrue(engine.needs_service())

    def test_needs_service_false(self):
        warning_light_is_on = False
        engine = SternmanEngine(warning_light_is_on)
        self.assertFalse(engine.needs_service())

if __name__ == "__main__":
    unittest.main()
