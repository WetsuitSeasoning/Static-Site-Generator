import unittest
from leafnode import *

class TestLeafNode(unittest.TestCase):
    def test_constructor(self):
        node = LeafNode("this is a tag", "this is a value", {"key1": "value1"})
        result = node.__repr__()
        expected_result = "tag= this is a tag, value= this is a value, children= None, props= {'key1': 'value1'}"
        self.assertEqual(result, expected_result)
    
    def test_to_html_empty_tag(self):
        node = LeafNode(None, "this is a value", None)
        result = node.to_html()
        expected_result = "this is a value"
        self.assertEqual(result, expected_result)

    def test_to_html_empty_value(self):
        node = LeafNode("p", None, None)
        with self.assertRaises(ValueError):
            node.to_html()

    def test_to_html_empty_props(self):
        node = LeafNode("p", "this is a value", None)
        result = node.to_html()
        expected_result = "<p>this is a value</p>"
        self.assertEqual(result, expected_result)

    def test_to_html(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        result = node.to_html()
        expected_result = "<a href=\"https://www.google.com\">Click me!</a>"
        self.assertEqual(result, expected_result)




if __name__ == "__main__":
    unittest.main()