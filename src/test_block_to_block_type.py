import unittest
from block_type import BlockType, block_to_block_type

class TestBlock(unittest.TestCase):
    def test_block_heading(self):
        text = "# This is a heading"
        self.assertEqual(block_to_block_type(text), BlockType.HEADING)
    
    def test_block_code(self):
        text = "```\nprint('Hello')\n```"
        self.assertEqual(block_to_block_type(text), BlockType.CODE)
    
    def test_block_quote(self):
        text = "> This is a quote"
        self.assertEqual(block_to_block_type(text), BlockType.QUOTE)
    
    def test_unordered_list(self):
        text = "- Item 1\n- Item 2\n- Item 3"
        self.assertEqual(block_to_block_type(text), BlockType.UNORDERED_LIST)

    def test_ordered_list(self):
        text = "1. This should be ordered\n2. Second item\n3. Third item"
        self.assertEqual(block_to_block_type(text), BlockType.ORDERED_LIST)


if __name__ == "__main__":
    unittest.main()


