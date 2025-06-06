from leafnode import LeafNode
import unittest

class TestCases(unittest.TestCase):
    def test_leaf_to_html(self):
        node = LeafNode("Hello, world!", "p")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("Anchor Text", "a")
        self.assertEqual(node.to_html(), "<a>Anchor Text</a>")

    def test_leaf_to_html_div(self):
        node = LeafNode("This is used to divide sections of your page", "div")
        self.assertEqual(node.to_html(), "<div>This is used to divide sections of your page</div>")

    def test_leaf_to_head(self):
        node = LeafNode("This contains meta data", "head")
        self.assertEqual(node.to_html(), "<head>This contains meta data</head>")
