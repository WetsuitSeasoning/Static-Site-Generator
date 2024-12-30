import unittest
from block_markdown import markdown_to_blocks, block_to_blocktype

class TestBlockMarkdown(unittest.TestCase):
    def test_markdown_to_blocks_basic(self):
        markdown = "This is a paragraph. \n\nThis is another paragraph."
        expected = ["This is a paragraph.", "This is another paragraph."]
        self.assertEqual(markdown_to_blocks(markdown), expected)

    def test_markdown_to_blocks_empty(self):
        markdown = ""
        expected = []
        self.assertEqual(markdown_to_blocks(markdown), expected)

    def test_markdown_to_blocks_single(self):
        markdown = "This is a single block with no double newlines."
        expected = ["This is a single block with no double newlines."]
        self.assertEqual(markdown_to_blocks(markdown), expected)

    def test_markdown_to_blocks_multiple_with_whitespaces(self):
        markdown = "This is a paragraph with trailing whitespace. \n\n This is another paragraph with leading and trailing whitespace. \n\n This is a third paragraph with leading whitespace."
        expected = ["This is a paragraph with trailing whitespace.", "This is another paragraph with leading and trailing whitespace.", "This is a third paragraph with leading whitespace."]
        self.assertEqual(markdown_to_blocks(markdown), expected)

    def test_markdown_to_blocks_single_newlines(self):
        markdown = "This is line 1.\nThis is line 2.\nThis is line 3."
        expected = ["This is line 1.\nThis is line 2.\nThis is line 3."]
        self.assertEqual(markdown_to_blocks(markdown), expected)

    def test_markdown_to_blocks_single_newline_multiple_blocks(self):
        markdown = "This is line 1.\nThis is line 2.\nThis is line 3.\n\nThis is another block."
        expected = ["This is line 1.\nThis is line 2.\nThis is line 3.", "This is another block."]
        self.assertEqual(markdown_to_blocks(markdown), expected)

    def test_markdown_to_blocks_mulitple_consecutive_newlines(self):
        markdown = "This is block 1.\n\n\n\nThis is block 2."
        expected = ["This is block 1.", "This is block 2."]
        self.assertEqual(markdown_to_blocks(markdown), expected)

    def test_markdown_to_blocks_only_newlines(self):
        markdown = "\n\n\n\n\n\n\n\n"
        expected = []
        self.assertEqual(markdown_to_blocks(markdown), expected)

    def test_block_to_blocktype_paragraph(self):
        block = "This is a paragraph."
        expected = "paragraph"
        self.assertEqual(block_to_blocktype(block), expected)

    def test_block_to_blocktype_heading(self):
        block = "# This is a heading"
        expected = "heading"
        self.assertEqual(block_to_blocktype(block), expected)

    def test_block_to_blocktype_code(self):
        block = "```\nThis is code\n```"
        expected = "code"
        self.assertEqual(block_to_blocktype(block), expected)

    def test_block_to_blocktype_quote(self):
        block = "> This is a quote.\n> This is another quote."
        expected = "quote"
        self.assertEqual(block_to_blocktype(block), expected)

    def test_block_to_blocktype_unordered_list_asterisk(self):
        block = "* This is an unordered list item\n* This is another unordered list item"
        expected = "unordered_list"
        self.assertEqual(block_to_blocktype(block), expected)

    def test_block_to_blocktype_unordered_list_dash(self):
        block = "- This is an unordered list item\n- This is another unordered list item"
        expected = "unordered_list"
        self.assertEqual(block_to_blocktype(block), expected)

    def test_block_to_blocktype_ordered_list(self):
        block = "1. This is an ordered list item\n2. This is another ordered list item"
        expected = "ordered_list"
        self.assertEqual(block_to_blocktype(block), expected)

    def test_block_to_blocktype_mixed_list(self):
        block = "1. This is an ordered list item\n* This is an unordered list item"
        expected = "paragraph"
        self.assertEqual(block_to_blocktype(block), expected)

    def test_block_to_blocktype_mixed_list_2(self):
        block = "* This is an unordered list item\n1. This is an ordered list item"
        expected = "paragraph"
        self.assertEqual(block_to_blocktype(block), expected)

    def test_block_to_blocktype_code_without_closing(self):
        block = "```\nThis is code"
        expected = "paragraph"
        self.assertEqual(block_to_blocktype(block), expected)

if __name__ == "__main__":
    unittest.main()