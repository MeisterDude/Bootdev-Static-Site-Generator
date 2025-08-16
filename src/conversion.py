
from textnode import TextType
from htmlnode import LeafNode


def text_node_to_html_node(text_node):
    match (text_node.text_type):
        case TextType.PLAIN:
            return LeafNode(tag=None, value=text_node.text)
        case TextType.BOLD:
            return LeafNode(tag="b", value=text_node.text)
        case TextType.ITALIC:
            return LeafNode(tag="i", value=text_node.text)
        case TextType.CODE:
            return LeafNode(tag="code", value=text_node.text)
        case TextType.LINK:
            if not text_node.url:
                raise ValueError("Link text node must have a URL")
            return LeafNode(tag="a", value=text_node.text, props={"href": text_node.url})
        case TextType.IMAGE:
            if not text_node.url:
                raise ValueError("Image text node must have a URL")
            return LeafNode(tag="img", value="", props={"src": text_node.url, "alt": text_node.text})
        case _:
            raise ValueError(f"Unknown text type: {text_node.text_type}")
        
def split_nodes_delimiter(old_nodes, delimiter, text_type):
    pass
