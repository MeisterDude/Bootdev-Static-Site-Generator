
import unittest

from conversion import text_node_to_html_node
from textnode import TextNode, TextType
from htmlnode import LeafNode


class Test_Text_to_HTML(unittest.TestCase):

    def test_text_node_to_html_node(self):
        node = TextNode("This is a text node", TextType.PLAIN)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

        bold_node = TextNode("This is bold", TextType.BOLD)
        html_bold_node = text_node_to_html_node(bold_node)
        self.assertEqual(html_bold_node.tag, "b")
        self.assertEqual(html_bold_node.value, "This is bold") 

        italic_node = TextNode("This is italic", TextType.ITALIC)
        html_italic_node = text_node_to_html_node(italic_node)
        self.assertEqual(html_italic_node.tag, "i")
        self.assertEqual(html_italic_node.value, "This is italic")

        code_node = TextNode("This is code", TextType.CODE)
        html_code_node = text_node_to_html_node(code_node)
        self.assertEqual(html_code_node.tag, "code")
        self.assertEqual(html_code_node.value, "This is code")

        link_node = TextNode("This is a link", TextType.LINK, url="http://example.com")
        html_link_node = text_node_to_html_node(link_node)
        self.assertEqual(html_link_node.tag, "a")
        self.assertEqual(html_link_node.value, "This is a link")
        self.assertEqual(html_link_node.props, {"href": "http://example.com"})

        image_node = TextNode("This is an image", TextType.IMAGE, url="http://example.com/image.png")
        html_image_node = text_node_to_html_node(image_node)
        self.assertEqual(html_image_node.tag, "img")
        self.assertEqual(html_image_node.value, "")
        self.assertEqual(html_image_node.props, {"src": "http://example.com/image.png", "alt": "This is an image"})

    def test_invalid_text_node(self):
        with self.assertRaises(ValueError):
            text_node_to_html_node(TextNode("This is a link without URL", TextType.LINK))

        with self.assertRaises(ValueError):
            text_node_to_html_node(TextNode("This is an image without URL", TextType.IMAGE))
        
        with self.assertRaises(ValueError):
            text_node_to_html_node(TextNode("Unknown type", "unknown_type"))