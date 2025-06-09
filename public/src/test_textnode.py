import unittest

from textnode import *


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is not a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_url(self):
        node = TextNode("This is a text node", TextType.LINK)
        self.assertIsNone(node.url)

    def test_url_not_null(self):
        node = TextNode("This is a text node", TextType.LINK, url="test.org")
        self.assertIsNotNone(node.url)

    def test_text_type(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")
    
    def test_image(self):
        text_node = TextNode("A cute cat", TextType.IMAGE, url="cat.png")
        leaf_node = text_node_to_html_node(text_node)
        self.assertIsInstance(leaf_node, LeafNode)
        self.assertEqual(leaf_node.tag, "img")
        self.assertEqual(leaf_node.value, "")
        self.assertEqual(leaf_node.props, {"src": "cat.png", "alt": "A cute cat"})
        self.assertEqual(leaf_node.to_html(), '<img src="cat.png" alt="A cute cat">')







if __name__ == "__main__":
    unittest.main()