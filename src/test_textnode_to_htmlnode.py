import unittest
from textnode_to_htmlnode import *
from leafnode import LeafNode


class TestHTMLNode(unittest.TestCase):
    def test_text_node_to_html_node_basic_text(self):
        text = "Hello World"
        text_node = TextNode(text, TextType.TEXT)
        html_node = text_node_to_html_node(text_node)
        #test properties
        assert html_node.tag is None
        assert html_node.value == text
        assert html_node.props is None
        #test HTML output
        assert html_node.to_html() == text

    def test_text_node_to_html_node_bold(self):
        text = "Hello World"
        text_node = TextNode(text, TextType.BOLD)
        html_node = text_node_to_html_node(text_node)
        #test properties
        assert html_node.tag == "b"
        assert html_node.value == text
        assert html_node.props == None
        #test HTML output
        assert html_node.to_html() == "<b>Hello World</b>"

    def test_text_node_to_html_node_italic(self):
        text = "Hello World"
        text_node = TextNode(text, TextType.ITALIC)
        html_node = text_node_to_html_node(text_node)
        #test properties
        assert html_node.tag == "i"
        assert html_node.value == text
        assert html_node.props == None
        #test HTML output
        assert html_node.to_html() == "<i>Hello World</i>"

    def test_text_node_to_html_node_code(self):
        text = "some code"
        text_node = TextNode(text, TextType.CODE)
        html_node = text_node_to_html_node(text_node)
        #test properties
        assert html_node.tag == "code"
        assert html_node.value == text
        assert html_node.props == None
        #test HTML output
        assert html_node.to_html() == "<code>some code</code>"

    def test_text_node_to_html_node_link(self):
        text = "Click me!"
        url = "www.google.com"
        text_node = TextNode(text, TextType.LINK, url)
        html_node = text_node_to_html_node(text_node)
        #test properties
        assert html_node.tag == "a"
        assert html_node.value == "Click me!"
        assert html_node.props == {"href": "www.google.com"}
        #test HTML output
        assert html_node.to_html() == "<a href=\"www.google.com\">Click me!</a>"

    def test_text_node_to_html_node_image(self):
        url = "www.virus.com/totally_not_a_virus.png"
        alt_text = "Click here to win"
        text_node = TextNode(alt_text, TextType.IMAGE, url)
        html_node = text_node_to_html_node(text_node)
        #test properties
        assert html_node.tag == "img"
        assert html_node.value == ""
        assert html_node.props == {"src": url, "alt": alt_text}
        #test HTML output
        assert html_node.to_html() == '<img src="www.virus.com/totally_not_a_virus.png" alt="Click here to win">'

    def test_text_node_to_html_node_invalid_type(self):
        text = "Hello World"
        text_node = TextNode(text, "not_a_valid_type")
        with self.assertRaises(ValueError):
            html_node = text_node_to_html_node(text_node)

if __name__ == "__main__":
    unittest.main()