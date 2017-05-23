from unittest import TestCase


class TestHas_unique_chars(TestCase):
    def test_has_unique_chars(self):
        try:
            from build import has_unique_chars
        except ImportError:
            self.assertFalse("No function found")

        self.assertEqual(has_unique_chars(None), False)
        self.assertEqual(has_unique_chars(''), True)
        self.assertEqual(has_unique_chars('foo'), False)
        self.assertEqual(has_unique_chars('bar'), True)
