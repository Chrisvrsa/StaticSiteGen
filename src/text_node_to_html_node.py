from leafnode import LeafNode
from textnode import TextNode, TextType

node = TextNode("Hello World", TextType.IMAGE)

def text_node_to_html_node(text_node):
    match text_node.text_type:
        case TextType.TEXT:
            return LeafNode(None, text_node.text, props=None)
        case TextType.BOLD:
            return LeafNode("b", text_node.text, props=None)
        case TextType.ITALIC:
            return LeafNode("i", text_node.text, props=None)
        case TextType.CODE:
            return LeafNode("code", text_node.text, props=None)
        case TextType.LINK:
            return LeafNode("a", text_node.text, props={"href": text_node.url})
        case TextType.IMAGE:
            return LeafNode("img", "", props={"alt": text_node.text, "src": text_node.url})
        case _:
            raise ValueError(f"Unknown text type: {text_node.text_type}")

