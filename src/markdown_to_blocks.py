
md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""


def markdown_to_blocks(markdown):
    text_list = [item.strip() for item in markdown.split('\n\n') if item.strip() != ""]
    return text_list

lists = markdown_to_blocks(md)

print(lists)