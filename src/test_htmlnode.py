
import unittest

from htmlnode import HTMLNode, LeafNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode(tag="div", props={"class": "container", "id": "main"})
        self.assertEqual(node.props_to_html(), ' class="container" id="main"')

        node_empty = HTMLNode(tag="span")
        self.assertEqual(node_empty.props_to_html(), "")

        node_no_props = HTMLNode(tag="p", props=None)
        self.assertEqual(node_no_props.props_to_html(), "")

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
        node_no_value = LeafNode("p", "")
        with self.assertRaises(ValueError):
            node_no_value.to_html()
        node_with_props = LeafNode("p", "Hello, world!", props={"class": "text"})
        self.assertEqual(node_with_props.to_html(), '<p class="text">Hello, world!</p>')
