import unittest
from parentnode import *
from leafnode import *

class TestParentNode(unittest.TestCase):
    def test_constructor(self):
        node = ParentNode("p", [LeafNode("b", "this is some text", None)],None)
        result = node.__repr__()
        expected_result = "tag= p, value= None, children= [tag= b, value= this is some text, children= None, props= None], props= None"
        self.assertEqual(result, expected_result)

    def test_constructor_empty_children(self):
        test_list = []
        with self.assertRaises(ValueError):
            ParentNode("p", test_list, None)

    def test_constructor_empty_tag(self):
        with self.assertRaises(ValueError):
            ParentNode(None, [LeafNode("a", "b", None)], None)

    def test_to_html_single_child(self):
        node = ParentNode("p", [LeafNode("b", "this is some text", None)], None)
        result = node.to_html()
        expected_result = "<p><b>this is some text</b></p>"
        self.assertEqual(result, expected_result)

    def test_to_html_two_children(self):
        node = ParentNode("p", [LeafNode("a", "Click me!", {"href": "www.google.com"}), LeafNode(None, "this is some text", None)], None)
        result = node.to_html()
        expected_result = "<p><a href=\"www.google.com\">Click me!</a>this is some text</p>"
        self.assertEqual(result, expected_result)

    def test_to_html_nested_childred(self):
        node = ParentNode(
            "h1",
            [LeafNode(None, "this is some text", None),
             ParentNode("p", [
                 LeafNode("b", "this is some text", None),
                 LeafNode("a", "Click me!", {"href": "www.google.com"})
             ], None)
            ],
            None
        )
        result = node.to_html()
        expected_result = "<h1>this is some text<p><b>this is some text</b><a href=\"www.google.com\">Click me!</a></p></h1>"
        self.assertEqual(result, expected_result)

if __name__ == "__main__":
    unittest.main()