import unittest
from htmlnode import *

class TestHTMLNode(unittest.TestCase):
    def test_only_tag(self):
        node = HTMLNode("this is a tag")
        result = node.__repr__()
        expected_result = "tag= this is a tag, value= None, children= None, props= None"
        self.assertEqual(result, expected_result)

    def test_only_value(self):
        node = HTMLNode(None, "this is a value")
        result = node.__repr__()
        expected_result = "tag= None, value= this is a value, children= None, props= None"
        self.assertEqual(result, expected_result)

    def test_only_children(self):
        test_list = ["child 1", "child 2", "child 3"]
        node = HTMLNode(None, None, test_list)
        result = node.__repr__()
        expected_result = f"tag= None, value= None, children= {test_list}, props= None"
        self.assertEqual(result, expected_result)

    def test_only_props(self):
        test_props = {"key 1": "value 1", "key 2": "value 2", "key 3": "value 3"}
        node = HTMLNode(None, None, None, test_props)
        result = node.__repr__()
        expected_result = f"tag= None, value= None, children= None, props= {test_props}"
        self.assertEqual(result, expected_result)

    def test_empty_props_to_HTML(self):
        node = HTMLNode(None, None, None, None)
        result = node.props_to_html()
        expected_result = ""
        self.assertEqual(result, expected_result)

    def test_props_to_HTML(self):
        test_props = {"key1": "value1", "key2": "value2", "key3": "value3"}
        node = HTMLNode(None, None, None, test_props)
        result = node.props_to_html()
        expected_result = " key1=\"value1\" key2=\"value2\" key3=\"value3\""
        self.assertEqual(result, expected_result)

    def test_repr(self):
        test_children = ["child1", "child2", "child 3"]
        test_props = {"key1": "value1", "key2": "value2", "key3": "value3"}
        node = HTMLNode("this is a tag", "this is a value", test_children, test_props)
        result = node.__repr__()
        expected_result = "tag= this is a tag, value= this is a value, children= ['child1', 'child2', 'child 3'], props= {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}"
        self.assertEqual(result, expected_result)

if __name__ == "__main__":
    unittest.main()