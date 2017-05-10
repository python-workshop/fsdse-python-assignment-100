import unittest


class MyTestCase(unittest.TestCase):
    # test file is present
    # 1 number should not be 0
    # 2 number should not be greater than 100
    # pass a number and check if value is coming back is factorial
    def test_file_present_check(self):
        try:
            from build import build
        except ImportError:
            self.assertFalse("Import failed")

    def test_number_should_not_be_less_than_0(self):
        try:
            from build import build
        except ImportError:
            self.assertFalse("Import failed")

        result = build(0)
        self.assertEqual("1 - 100 is only acceptable", result)

    def test_number_should_not_be_greater_than_100(self):
        try:
            from build import build
        except ImportError:
            self.assertFalse("Import failed")

        result = build(100)
        self.assertEqual("1 - 100 is only acceptable", result)

    def test_factorial_of_number(self):
        try:
            from build import build
        except ImportError:
            self.assertFalse("Import failed")

        result = build(5)
        self.assertEqual([1,2,6,24,120], result)