import unittest
from step_counter import StepCounter

class TestStepCounter(unittest.TestCase):
    
    def setUp(self):
        self.counter = StepCounter()
        self.counter.add_daily_steps('2024-09-01', 8000, 250)
        self.counter.add_daily_steps('2024-09-02', 9500, 280)
        self.counter.add_daily_steps('2024-09-03', 12000, 300)
    
    def test_total_weekly_steps(self):
        self.assertEqual(self.counter.total_weekly_steps(), 29500)
    
    def test_activity_level(self):
        self.assertEqual(self.counter.activity_level(), "High")

if __name__ == '__main__':
    unittest.main()
