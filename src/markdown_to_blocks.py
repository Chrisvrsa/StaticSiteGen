
md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""

def markdown_to_blocks(markdown):
    # returns a list
    # strip excessive spaces
    # /n/n is allowed. /n is also allowed. Anything above two new lines is not allowed
    text_list = markdown.split('\n\n')
    print(text_list)
    for i, item in enumerate(text_list):
        text_list[i] = item.strip()
        if item.startswith('\n'):
            text_list[i] = item.replace('\n', "")

    return text_list

lists = markdown_to_blocks(md)

print(lists)