import unittest
from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_eq_different_textType(self):
        node = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_empty_string(self):
        node = TextNode("", TextType.TEXT)
        node2 = TextNode("This is a text node", TextType.TEXT)
        self.assertNotEqual(node, node2)

    def test_url_none(self):
        node = TextNode("This is a text node", TextType.BOLD, url=None)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_different_urls(self):
        node = TextNode("This is a text node", TextType.BOLD, url="http://example.com")
        node2 = TextNode("This is a text node", TextType.BOLD, url="http://another.com")
        self.assertNotEqual(node, node2)

    def test_eq_method(self):
        node = TextNode("This is a text node", TextType.TEXT, url="www.frontend.dev")
        node2 = TextNode("This is a text node", TextType.TEXT, url="www.frontend.dev")
        result = node.__eq__(node2)
        self.assertEqual(result, True)

    def test_repr(self):
        node = TextNode("This is a text node", TextType.BOLD, url="http://example.com")
        result = repr(node)
        # Assume this is the expected format
        expected_repr = "TextNode(This is a text node, bold, http://example.com)"
        self.assertEqual(result, expected_repr)

    def test_repr_with_no_url(self):
        node = TextNode("This is a text node", TextType.BOLD)
        result = repr(node)
        expected_repr = "TextNode(This is a text node, bold, None)"
        self.assertEqual(result, expected_repr)

if __name__ == "__main__":
    unittest.main()