import unittest
from block_markdown import markdown_to_blocks, block_to_blocktype, markdown_to_html_node

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

    def test_markdown_to_html_node_paragraph(self):
        markdown = "This is a paragraph."
        expected = "<div><p>This is a paragraph.</p></div>"
        self.assertEqual(markdown_to_html_node(markdown).to_html(), expected)

    def test_markdown_to_html_node_heading(self):
        markdown = "# This is a heading"
        expected = "<div><h1>This is a heading</h1></div>"
        self.assertEqual(markdown_to_html_node(markdown).to_html(), expected)

    def test_markdown_to_html_node_heading_2(self):
        markdown = "## This is a heading"
        expected = "<div><h2>This is a heading</h2></div>"
        self.assertEqual(markdown_to_html_node(markdown).to_html(), expected)

    def test_markdown_to_html_node_heading_3(self):
        markdown = "### This is a heading"
        expected = "<div><h3>This is a heading</h3></div>"
        self.assertEqual(markdown_to_html_node(markdown).to_html(), expected)

    def test_markdown_to_html_node_heading_4(self):
        markdown = "#### This is a heading"
        expected = "<div><h4>This is a heading</h4></div>"
        self.assertEqual(markdown_to_html_node(markdown).to_html(), expected)

    def test_markdown_to_html_node_heading_5(self):
        markdown = "##### This is a heading"
        expected = "<div><h5>This is a heading</h5></div>"
        self.assertEqual(markdown_to_html_node(markdown).to_html(), expected)

    def test_markdown_to_html_node_heading_6(self):
        markdown = "###### This is a heading"
        expected = "<div><h6>This is a heading</h6></div>"
        self.assertEqual(markdown_to_html_node(markdown).to_html(), expected)

    def test_markdown_to_html_node_heading_7(self):
        markdown = "####### This is a heading"
        with self.assertRaises(ValueError):
            markdown_to_html_node(markdown)

    def test_markdown_to_html_node_code(self):
        markdown = "```\nThis is code\n```"
        expected = "<div><pre><code>This is code</code></pre></div>"
        self.assertEqual(markdown_to_html_node(markdown).to_html(), expected)

    def test_markdown_to_html_node_code_with_markdown(self):
        markdown = "```\ndef hello():\n    print('**not bold**')\n```"
        expected = "<div><pre><code>def hello():\n    print('**not bold**')</code></pre></div>"
        self.assertEqual(markdown_to_html_node(markdown).to_html(), expected)

    def test_markdown_to_html_node_code_multiline(self):
        markdown = "```\ndef example():\n    x = 1\n    y = 2\n    return x + y\n```"
        expected = "<div><pre><code>def example():\n    x = 1\n    y = 2\n    return x + y</code></pre></div>"
        self.assertEqual(markdown_to_html_node(markdown).to_html(), expected)

    def test_markdown_to_html_node_quote(self):
        markdown = "> This is a quote"
        expected = "<div><blockquote>This is a quote</blockquote></div>"
        self.assertEqual(markdown_to_html_node(markdown).to_html(), expected)

    def test_markdown_to_html_node_quote_multiline(self):
        markdown = "> My fellow Americans:\n> Ask not what your country can do for you\n> Ask what you can do for your country"
        expected = "<div><blockquote>My fellow Americans:\nAsk not what your country can do for you\nAsk what you can do for your country</blockquote></div>"
        self.assertEqual(markdown_to_html_node(markdown).to_html(), expected)

    def test_markdown_to_html_node_quote_multiline_with_markdown(self):
        markdown = "> This is **bold**\n> This is *italic*\n> This is `code`"
        expected = "<div><blockquote>This is <b>bold</b>\nThis is <i>italic</i>\nThis is <code>code</code></blockquote></div>"
        self.assertEqual(markdown_to_html_node(markdown).to_html(), expected)

    def test_markdown_to_html_node_unordered_list_asterisk(self):
        markdown = "* This is an item\n* This is another item"
        expected = "<div><ul><li>This is an item</li><li>This is another item</li></ul></div>"
        self.assertEqual(markdown_to_html_node(markdown).to_html(), expected)

    def test_markdown_to_html_node_unordered_list_dash(self):
        markdown = "- This is an item\n- This is another item"
        expected = "<div><ul><li>This is an item</li><li>This is another item</li></ul></div>"
        self.assertEqual(markdown_to_html_node(markdown).to_html(), expected)

    def test_markdown_to_html_node_unordered_list_plus(self):
        markdown = "+ This is an item\n+ This is another item"
        expected = "<div><ul><li>This is an item</li><li>This is another item</li></ul></div>"
        self.assertEqual(markdown_to_html_node(markdown).to_html(), expected)

    def test_markdown_to_html_node_unordered_list_with_markdown(self):
        markdown = "- Item with **bold**\n- Item with *italic*\n- Item with `code`"
        expected = "<div><ul><li>Item with <b>bold</b></li><li>Item with <i>italic</i></li><li>Item with <code>code</code></li></ul></div>"
        self.assertEqual(markdown_to_html_node(markdown).to_html(), expected)

    def test_markdown_to_html_node_ordered_list(self):
        markdown = "1. This is an item\n2. This is another item"
        expected = "<div><ol><li>This is an item</li><li>This is another item</li></ol></div>"
        self.assertEqual(markdown_to_html_node(markdown).to_html(), expected)

    def test_markdown_to_html_node_ordered_list_with_markdown(self):
        markdown = "1. Item with **bold**\n2. Item with *italic*\n3. Item with `code`"
        expected = "<div><ol><li>Item with <b>bold</b></li><li>Item with <i>italic</i></li><li>Item with <code>code</code></li></ol></div>"
        self.assertEqual(markdown_to_html_node(markdown).to_html(), expected)

    def test_markdown_to_html_node_ordered_list_random_numbers(self):
        markdown = "1. First item\n5. Second item\n2. Third item"
        expected = "<div><ol><li>First item</li><li>Second item</li><li>Third item</li></ol></div>"
        self.assertEqual(markdown_to_html_node(markdown).to_html(), expected)

    def test_markdown_to_html_node_ordered_list_double_digits(self):
        markdown = "10. First item\n11. Second item\n12. Third item"
        expected = "<div><ol><li>First item</li><li>Second item</li><li>Third item</li></ol></div>"
        self.assertEqual(markdown_to_html_node(markdown).to_html(), expected)

    def test_markdown_to_html_node_mixed_list_types(self):
        markdown = "1. First item\n* Second item\n3. Third item"
        expected = "<div><p>1. First item\n* Second item\n3. Third item</p></div>"
        self.assertEqual(markdown_to_html_node(markdown).to_html(), expected)

    def test_markdown_to_html_node_multiple_blocks(self):
        markdown = "# Heading\n\nParagraph text\n\n> A quote"
        expected = "<div><h1>Heading</h1><p>Paragraph text</p><blockquote>A quote</blockquote></div>"
        self.assertEqual(markdown_to_html_node(markdown).to_html(), expected)

    def test_markdown_to_html_node_nested_unordered_lists(self):
        markdown = "* First item\n  * First nested item\n  * Second nested item\n* Second item"
        expected = "<div><ul><li>First item<ul><li>First nested item</li><li>Second nested item</li></ul></li><li>Second item</li></ul></div>"
        self.assertEqual(markdown_to_html_node(markdown).to_html(), expected)

    def test_markdown_to_html_node_nested_ordered_lists(self):
        markdown = "1. First item\n  1. First nested item\n  2. Second nested item\n2. Second item"
        expected = "<div><ol><li>First item<ol><li>First nested item</li><li>Second nested item</li></ol></li><li>Second item</li></ol></div>"
        self.assertEqual(markdown_to_html_node(markdown).to_html(), expected)

if __name__ == "__main__":
    unittest.main()