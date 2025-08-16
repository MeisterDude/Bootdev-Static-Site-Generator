
import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


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

        node_no_tag = LeafNode(None, "Just text")
        self.assertEqual(node_no_tag.to_html(), "Just text")


    def test_parent_to_html(self):
        child1 = LeafNode("span", "Child 1")
        child2 = LeafNode("span", "Child 2")
        parent = ParentNode(tag="div", children=[child1, child2])
        self.assertEqual(parent.to_html(), "<div><span>Child 1</span><span>Child 2</span></div>")
        
        parent_no_tag = ParentNode(tag=None, children=[child1, child2])
        with self.assertRaises(ValueError):
            parent_no_tag.to_html()
        
        parent_no_children = ParentNode(tag="div", children=[])
        with self.assertRaises(ValueError):
            parent_no_children.to_html()

        grandparent = ParentNode(tag="section", children=[parent])
        self.assertEqual(grandparent.to_html(), "<section><div><span>Child 1</span><span>Child 2</span></div></section>")
