import unittest

from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_equal(self):
        node = TextNode("This is a text node", TextType.BOLD, "www.boot.dev.com")
        node2 = TextNode("This is a text node", TextType.IMAGE, "www.boot.dev.com")
        self.assertNotEqual(node, node2)

    def test_not_equal_types_and_url(self):
        node = TextNode("This is a text node", TextType.BOLD, None)
        node2 = TextNode("This is a text node", TextType.BOLD, "www.boot.dev.com")
        self.assertNotEqual(node, node2)

if __name__ == '__main__':
    # run main in unittest
    unittest.main()