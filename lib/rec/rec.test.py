import unittest
from rec import Rec

class RecTestSuite( unittest.TestCase ):
    def setUp(self):
        self.r = Rec()

    def test_filter_module(self):
        self.assertEqual(
            self.r.filter.__module__,
            'filter'
        )

    def test_text_module(self):
        self.assertEqual(
            self.r.text.__module__,
            'text'
        )

    def test_stack_module(self):
        self.assertEqual(
            self.r.stack.__module__,
            'stack'
        )

if __name__ == '__main__':
    unittest.main()
