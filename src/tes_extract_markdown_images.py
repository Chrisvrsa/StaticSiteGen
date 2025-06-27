import unittest
from extract_markdown_images import extract_markdown_links, extract_markdown_images

class TestMarkdownExtraction(unittest.TestCase):
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is a link in markdown: [alt text](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertEqual([("alt text", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_multiple_images(self):
        matches = extract_markdown_images(
            "![one](https://a.com/1.png) and ![two](https://a.com/2.jpg)"
        )
        self.assertEqual([
            ("one", "https://a.com/1.png"),
            ("two", "https://a.com/2.jpg")
        ], matches)

    def test_excludes_image_from_link_results(self):
        matches = extract_markdown_links(
            "Regular link: [site](https://site.com) and image ![pic](https://img.com/pic.png)"
        )
        self.assertEqual([
            ("site", "https://site.com")
        ], matches)

if __name__ == "__main__":
    unittest.main()