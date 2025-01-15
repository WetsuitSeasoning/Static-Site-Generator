import unittest
from markdown import extract_title

class TestExtractTitle(unittest.TestCase):
    def test_single_line(self):
        self.assertEqual(extract_title("# Hello"), "Hello")

if __name__ == "__main__":
    unittest.main()