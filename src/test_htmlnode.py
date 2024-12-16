import unittest
from htmlnode import *

class TestHTMLNode(unittest.TestCase):
    def test_only_tag(self):
        node = HTMLNode("this is a tag")
        result = node.tag
        expected_result = "this is a tag"
        self.assertEqual(result, expected_result)

    def test_only_value(self):
        node = HTMLNode(None, "this is a value")
        result = node.value
        expected_result = "this is a value"
        self.assertEqual(result, expected_result)

    def test_only_children(self):
        test_list = ["child 1", "child 2", "child 3"]
        node = HTMLNode(None, None, test_list)
        result = node.children
        self.assertEqual(result, test_list)

    def test_only_props(self):
        test_props = {"key 1": "value 1", "key 2": "value 2", "key 3": "value 3"}
        node = HTMLNode(None, None, None, test_props)
        result = node.props
        self.assertEqual(result, test_props)

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
        expected_result = "tag= this is a tag\nvalue= this is a value\nchildren= ['child1', 'child2', 'child 3']\nprops= {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}"
        self.assertEqual(result, expected_result)

if __name__ == "__main__":
    unittest.main()