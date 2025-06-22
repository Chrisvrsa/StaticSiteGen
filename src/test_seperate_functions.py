import unittest
from textnode import TextNode, TextType
from leafnode import LeafNode
from text_node_to_html_node import text_node_to_html_node  # adjust if named differently

class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_text_node(self):
        node = TextNode("Hello", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "Hello")
        self.assertEqual(html_node.props, None)

    def test_bold_node(self):
        node = TextNode("Bold", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "Bold")

    def test_link_node(self):
        node = TextNode("Click here", TextType.LINK, url="https://boot.dev")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "Click here")
        self.assertEqual(html_node.props, {"href": "https://boot.dev"})

    def test_image_node(self):
        node = TextNode("Boot.dev Logo", TextType.IMAGE, url="logo.png")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.props, {"alt": "Boot.dev Logo", "src": "logo.png"})



    def test_invalid_type_raises(self):
        class FakeType:
            pass
        with self.assertRaises(ValueError):
            node = TextNode("Oops", FakeType())
            text_node_to_html_node(node)

if __name__ == '__main__':
    unittest.main()