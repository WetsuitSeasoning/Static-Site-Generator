import unittest
from markdown import extract_title

class TestExtractTitle(unittest.TestCase):
    def test_single_line(self):
        self.assertEqual(extract_title("# Hello"), "Hello")

    def test_multiple_lines(self):
        self.assertEqual(extract_title("# Hello\nWorld"), "Hello")

    def test_no_title(self):
        with self.assertRaises(ValueError):
            extract_title("Hello\nWorld")

    def test_no_space_after_hash(self):
        with self.assertRaises(ValueError):
            extract_title("#Hello")

    def test_no_newline(self):
        self.assertEqual(extract_title("# Hello"), "Hello")

    def test_leading_whitespace(self):
        self.assertEqual(extract_title("#   Hello"), "Hello")

    def test_trailing_whitespace(self):
        self.assertEqual(extract_title("# Hello   "), "Hello")

    def test_empty_string(self):
        with self.assertRaises(ValueError):
            extract_title("")

    def test_empty_title(self):
        self.assertEqual(extract_title("# "), "")

    def test_special_characters(self):
        self.assertEqual(extract_title("# Hello, world!"), "Hello, world!")

    def test_numbers_in_title(self):
        self.assertEqual(extract_title("# Hello123"), "Hello123")

    def test_only_hash(self):
        with self.assertRaises(ValueError):
            extract_title("#")

    def test_multiple_hashes(self):
        with self.assertRaises(ValueError):
            extract_title("## Hello")
    
    def test_hash_in_middle(self):
        self.assertEqual(extract_title("# Hello # World"), "Hello # World")

if __name__ == "__main__":
    unittest.main()