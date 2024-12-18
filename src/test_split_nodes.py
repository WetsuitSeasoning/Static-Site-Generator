import unittest
from split_nodes import split_nodes_delimiter
from textnode import TextNode, TextType

class TestSplitNodes(unittest.TestCase):
    def test_split_nodes_italic(self):
        nodes = [TextNode("This is *italic* text", TextType.TEXT)]
        delimiter = "*"
        text_type = TextType.ITALIC
        result = split_nodes_delimiter(nodes, delimiter, text_type)
        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" text", TextType.TEXT)
        ]
        self.assertEqual(result, expected)

    def test_split_nodes_bold(self):
        nodes = [TextNode("This is **bold** text", TextType.TEXT)]
        delimiter = "**"
        text_type = TextType.BOLD
        result = split_nodes_delimiter(nodes, delimiter, text_type)
        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" text", TextType.TEXT)
        ]
        self.assertEqual(result, expected)

    def test_split_nodes_code(self):
        nodes = [TextNode("This is 'code' text", TextType.TEXT)]
        delimiter = "'"
        text_type = TextType.CODE
        result = split_nodes_delimiter(nodes, delimiter, text_type)
        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("code", TextType.CODE),
            TextNode(" text", TextType.TEXT)
        ]
        self.assertEqual(result, expected)

    def test_split_nodes_multiple_italic(self):
        nodes = [
            TextNode("This is *italic* text", TextType.TEXT),
            TextNode(" and *another* one", TextType.TEXT)
        ]
        delimiter = "*"
        text_type = TextType.ITALIC
        result = split_nodes_delimiter(nodes, delimiter, text_type)
        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" text", TextType.TEXT),
            TextNode(" and ", TextType.TEXT),
            TextNode("another", TextType.ITALIC),
            TextNode(" one", TextType.TEXT)
        ]
        self.assertEqual(result, expected)

    def test_split_nodes_multiple_bold(self):
        nodes = [
            TextNode("This is **bold** text", TextType.TEXT),
            TextNode(" and **another** one", TextType.TEXT)
        ]
        delimiter = "**"
        text_type = TextType.BOLD
        result = split_nodes_delimiter(nodes, delimiter, text_type)
        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" text", TextType.TEXT),
            TextNode(" and ", TextType.TEXT),
            TextNode("another", TextType.BOLD),
            TextNode(" one", TextType.TEXT)
        ]
        self.assertEqual(result, expected)

    def test_split_nodes_multiple_code(self):
        nodes = [
            TextNode("This is 'code' text", TextType.TEXT),
            TextNode(" and 'another' one", TextType.TEXT)
        ]
        delimiter = "'"
        text_type = TextType.CODE
        result = split_nodes_delimiter(nodes, delimiter, text_type)
        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("code", TextType.CODE),
            TextNode(" text", TextType.TEXT),
            TextNode(" and ", TextType.TEXT),
            TextNode("another", TextType.CODE),
            TextNode(" one", TextType.TEXT)
        ]
        self.assertEqual(result, expected)

    def test_split_nodes_invalid_text_type(self):
        nodes = [TextNode("This is some text", "invalid_type")]
        delimiter = "*"
        text_type = TextType.ITALIC
        with self.assertRaises(ValueError):
            split_nodes_delimiter(nodes, delimiter, text_type)

    def test_split_nodes_uneven_delimiter_count(self):
        nodes = [TextNode("This is *italic text", TextType.TEXT)]
        delimiter = "*"
        text_type = TextType.ITALIC
        with self.assertRaises(ValueError):
            split_nodes_delimiter(nodes, delimiter, text_type)

    def test_split_nodes_empty_list(self):
        nodes = []
        delimiter = "'"
        text_type = TextType.CODE
        result = split_nodes_delimiter(nodes, delimiter, text_type)
        expected = []
        self.assertEqual(result, expected)

    def test_split_nodes_no_delimiters(self):
        nodes = [TextNode("This is plain text", TextType.TEXT)]
        delimiter = "'"
        text_type = TextType.CODE
        result = split_nodes_delimiter(nodes, delimiter, text_type)
        expected = [TextNode("This is plain text", TextType.TEXT)]
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()