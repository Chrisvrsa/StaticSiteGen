import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_cases(self):
        #basic test
        new_html_node = HTMLNode("101", "New HTML node", None, {"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(' href="https://www.google.com" target="_blank"', new_html_node.props_to_html())

    def test_more_props(self):
        # longer test
        new_html_node = HTMLNode(props={"src": "img_girl.jpg", "target": "_blank", "width": "200", "height": "400"})
        self.assertEqual(' src="img_girl.jpg" target="_blank" width="200" height="400"', new_html_node.props_to_html())

    def test_empty_props(self):
        # empty node
        new_empty_node = HTMLNode("102", "New HTML node two", "22")
        self.assertEqual('', new_empty_node.props_to_html())

    def test_empty_dict_and_children(self):
        new_html_node = HTMLNode("div", "content", None, {})
        self.assertEqual('', new_html_node.props_to_html())

if __name__ == '__main__':
    unittest.main()

