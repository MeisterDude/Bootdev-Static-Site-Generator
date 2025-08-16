
import unittest

from textnode import TextNode, TextType, split_nodes_delimiter


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
        node3 = TextNode("This is a different text node", TextType.BOLD)
        self.assertNotEqual(node, node3)
        node4 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node, node4)
        node5 = TextNode("This is a text node", TextType.BOLD, "https://example.com")
        self.assertNotEqual(node, node5)

    def test_split_nodes_delimiter(self):
        old_nodes = [TextNode("This is a text node", TextType.PLAIN)]
        new_nodes = split_nodes_delimiter(old_nodes, "**", TextType.BOLD)
        self.assertEqual(len(new_nodes), 1)
        self.assertEqual(new_nodes[0].text, "This is a text node")
        self.assertEqual(new_nodes[0].text_type, TextType.PLAIN)

        old_nodes = [TextNode("This is a **bold** text node", TextType.PLAIN)]
        new_nodes = split_nodes_delimiter(old_nodes, "**", TextType.BOLD)
        self.assertEqual(len(new_nodes), 3)
        self.assertEqual(new_nodes[0].text, "This is a ")
        self.assertEqual(new_nodes[0].text_type, TextType.PLAIN)
        self.assertEqual(new_nodes[1].text, "bold")
        self.assertEqual(new_nodes[1].text_type, TextType.BOLD)
        self.assertEqual(new_nodes[2].text, " text node")
        self.assertEqual(new_nodes[2].text_type, TextType.PLAIN)

        old_nodes = [TextNode("This is a **bold text node", TextType.PLAIN)]
        with self.assertRaises(ValueError):
            split_nodes_delimiter(old_nodes, "**", TextType.BOLD)

        old_nodes = [TextNode("This is an _italic_ text node", TextType.PLAIN), TextNode("This is a text node", TextType.PLAIN)]
        new_nodes = split_nodes_delimiter(old_nodes, "_", TextType.ITALIC)
        self.assertEqual(len(new_nodes), 4)
        self.assertEqual(new_nodes[0].text, "This is an ")
        self.assertEqual(new_nodes[0].text_type, TextType.PLAIN)
        self.assertEqual(new_nodes[1].text, "italic")
        self.assertEqual(new_nodes[1].text_type, TextType.ITALIC)
        self.assertEqual(new_nodes[2].text, " text node")
        self.assertEqual(new_nodes[2].text_type, TextType.PLAIN)
        self.assertEqual(new_nodes[3].text, "This is a text node")
        self.assertEqual(new_nodes[3].text_type, TextType.PLAIN)
        


if __name__ == "__main__":
    unittest.main()
