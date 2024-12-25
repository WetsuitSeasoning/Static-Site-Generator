import unittest
from inline_markdown import split_nodes_delimiter, split_nodes_image, split_nodes_link, extract_markdown_images, extract_markdown_links
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

    def test_extract_markdown_images_single(self):
        text = "This is some text with ![an image](https://example.com/image.png) in it."
        result = extract_markdown_images(text)
        expected = [("an image", "https://example.com/image.png")] # One image in the text, so we get a list of one tuple back
        self.assertEqual(result, expected)

    def test_extract_markdown_images_multiple(self):
        text = "This is some text with ![an image](https://example.com/image.png) and ![another image](https://example.com/another.png) in it."
        result = extract_markdown_images(text)
        expected = [
            ("an image", "https://example.com/image.png"),
            ("another image", "https://example.com/another.png")
        ] # Two images in the text, so we get a list of two tuples back
        self.assertEqual(result, expected)

    def test_extract_markdown_images_no_images(self):
        text = "This is some plain text."
        result = extract_markdown_images(text)
        expected = [] # No images in the text, so we get an empty list back
        self.assertEqual(result, expected)

    def test_extract_markdwon_images_no_alt_text(self):
        text = "This is some text with an image: ![](https://example.com/image.png)"
        result = extract_markdown_images(text)
        expected = [("", "https://example.com/image.png")] # Alt text is empty, so we get an empty string
        self.assertEqual(result, expected)

    def test_extract_markdown_image_no_url(self):
        text = "This is some text with an image: ![an image]()"
        result = extract_markdown_images(text)
        expected = [("an image", "")] # URL is empty, so we get an empty string
        self.assertEqual(result, expected)

    def test_extract_markdown_image_bad_syntax(self):
        text = "This is some text with an image: ![an image](https://example.com/image.png"
        result = extract_markdown_images(text)
        expected = []
        self.assertEqual(result, expected)

    def test_extract_markdown_link_single(self):
        text = "This is some text with [a link](www.example.com)"
        result = extract_markdown_links(text)
        expected = [("a link", "www.example.com")]
        self.assertEqual(result, expected)

    def test_extract_markdown_link_multiple(self):
        text = "This is some text with [a link](www.example.com) and [another link](www.example.org)"
        result = extract_markdown_links(text)
        expected = [("a link", "www.example.com"), ("another link", "www.example.org")]
        self.assertEqual(result, expected)

    def test_extract_markdown_link_no_links(self):
        text = "This is some text without links"
        result = extract_markdown_links(text)
        expected = []
        self.assertEqual(result, expected)

    def test_extract_markdown_link_no_link_text(self):
        text = "This is some text with a link: [](www.example.com)"
        result = extract_markdown_links(text)
        expected = [("", "www.example.com")]
        self.assertEqual(result, expected)

    def test_extract_markdown_link_no_url(self):
        text = "This is some text with a link: [a link]()"
        result = extract_markdown_links(text)
        expected = [("a link", "")]
        self.assertEqual(result, expected)

    def test_extract_markdown_link_bad_syntax(self):
        text = "This is some text with a link: [a link](www.example.com"
        result = extract_markdown_links(text)
        expected = []
        self.assertEqual(result, expected)

    def test_split_nodes_image_no_text(self):
        nodes = [TextNode("![This is an image](https://example.com/image.png)", TextType.TEXT)]
        result = split_nodes_image(nodes)
        expected = [
            TextNode("This is an image", TextType.IMAGE, "https://example.com/image.png")
        ]
        self.assertEqual(result, expected)

    def test_split_nodes_image_text_before(self):
        nodes = [
            TextNode("This is some text before ![an image](https://example.com/image.png)", TextType.TEXT),
        ]
        result = split_nodes_image(nodes)
        expected = [
            TextNode("This is some text before ", TextType.TEXT),
            TextNode("an image", TextType.IMAGE, "https://example.com/image.png")
        ]
        self.assertEqual(result, expected)

    def test_split_nodes_image_text_after(self):
        nodes = [
            TextNode("![This is an image](https://example.com/image.png) and some text after", TextType.TEXT),
        ]
        result = split_nodes_image(nodes)
        expected = [
            TextNode("This is an image", TextType.IMAGE, "https://example.com/image.png"),
            TextNode(" and some text after", TextType.TEXT)
        ]
        self.assertEqual(result, expected)

    def test_split_nodes_image_text_before_and_after(self):
        nodes = [
            TextNode("This is some text before ![an image](https://example.com/image.png) and some text after", TextType.TEXT),
        ]
        result = split_nodes_image(nodes)
        expected = [
            TextNode("This is some text before ", TextType.TEXT),
            TextNode("an image", TextType.IMAGE, "https://example.com/image.png"),
            TextNode(" and some text after", TextType.TEXT)
        ]
        self.assertEqual(result, expected)

    def test_split_nodes_image_multiple_images(self):
        nodes = [
            TextNode("![This is an image](https://example.com/image.png) and ![another image](https://example.com/another.png)", TextType.TEXT),
        ]
        result = split_nodes_image(nodes)
        expected = [
            TextNode("This is an image", TextType.IMAGE, "https://example.com/image.png"),
            TextNode(" and ", TextType.TEXT),
            TextNode("another image", TextType.IMAGE, "https://example.com/another.png")
        ]
        self.assertEqual(result, expected)

    def test_split_nodes_image_no_images(self):
        nodes = [
            TextNode("This is some plain text", TextType.TEXT),
        ]
        result = split_nodes_image(nodes)
        expected = [
            TextNode("This is some plain text", TextType.TEXT)
        ]
        self.assertEqual(result, expected)

    def test_split_nodes_image_other_text_type(self):
        nodes = [
            TextNode("This is some BOLD text", TextType.BOLD),
            TextNode("This is some text with ![an image](https://example.com/image.png) and some text after", TextType.TEXT),
        ]
        result = split_nodes_image(nodes)
        expected = [
            TextNode("This is some BOLD text", TextType.BOLD),
            TextNode("This is some text with ", TextType.TEXT),
            TextNode("an image", TextType.IMAGE, "https://example.com/image.png"),
            TextNode(" and some text after", TextType.TEXT)
        ]
        self.assertEqual(result, expected)

    def test_split_nodes_image_multiple_images_no_text_between(self):
        nodes = [
            TextNode("![This is an image](https://example.com/image.png)![another image](https://example.com/another.png)", TextType.TEXT),
        ]
        result = split_nodes_image(nodes)
        expected = [
            TextNode("This is an image", TextType.IMAGE, "https://example.com/image.png"),
            TextNode("another image", TextType.IMAGE, "https://example.com/another.png")
        ]
        self.assertEqual(result, expected)

    def test_split_nodes_image_invalid_text_type(self):
        nodes = [
            TextNode("This is some text", "invalid_type"),
        ]
        with self.assertRaises(ValueError):
            split_nodes_image(nodes)

    def test_split_nodes_image_empty_list(self):
        nodes = []
        result = split_nodes_image(nodes)
        expected = []
        self.assertEqual(result, expected)

    def test_split_nodes_image_invalid_markdown(self):
        nodes = [
            TextNode("This is some text with bad markdown: ![an image](https://example.com/image.png", TextType.TEXT),
        ]
        result = split_nodes_image(nodes)
        expected = [
            TextNode("This is some text with bad markdown: ![an image](https://example.com/image.png", TextType.TEXT),
        ]
        self.assertEqual(result, expected)

    def test_split_nodes_link_single(self):
        nodes = [TextNode("This is some text with [a link](www.example.com) in it.", TextType.TEXT)]
        result = split_nodes_link(nodes)
        expected = [
            TextNode("This is some text with ", TextType.TEXT),
            TextNode("a link", TextType.LINK, "www.example.com"),
            TextNode(" in it.", TextType.TEXT)
        ]
        self.assertEqual(result, expected)
        
    def test_split_nodes_link_multiple(self):
        nodes = [TextNode("This is some text with [a link](www.example.com) and [another link](www.example.org) in it.", TextType.TEXT)]
        result = split_nodes_link(nodes)
        expected = [
            TextNode("This is some text with ", TextType.TEXT),
            TextNode("a link", TextType.LINK, "www.example.com"),
            TextNode(" and ", TextType.TEXT),
            TextNode("another link", TextType.LINK, "www.example.org"),
            TextNode(" in it.", TextType.TEXT)
        ]
        self.assertEqual(result, expected)
       


if __name__ == "__main__":
    unittest.main()