import unittest
import sys     
sys.path.append('C:\\Users\\fahee\\Desktop\\Programming\\Virtual Internship\\lyft\\forage-lyft-task-3-model-answer-main\\engine')
from capulet_engine import CapuletEngine


class TestCapuletEngine(unittest.TestCase):
    def test_needs_service_true(self):
        current_mileage = 30001
        last_service_mileage = 0
        engine = CapuletEngine(current_mileage, last_service_mileage)
        self.assertTrue(engine.needs_service())

    def test_needs_service_false(self):
        current_mileage = 30000
        last_service_mileage = 0
        engine = CapuletEngine(current_mileage, last_service_mileage)
        self.assertFalse(engine.needs_service())

if __name__ == "__main__":
    unittest.main()
