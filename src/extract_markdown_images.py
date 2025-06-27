import re


def extract_markdown_images(markdown_text):
    list_of_tuples = re.findall(r"!\[(.*?)\]\((.*?)\)", markdown_text)
    return list_of_tuples

def extract_markdown_links(markdown_text):
    list_of_tuples = re.findall(r"(?<!!)\[(.*?)\]\((.*?)\)", markdown_text)
    return list_of_tuples

# Testing section
images = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJR.jpeg)"
print(extract_markdown_images(images))

link = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/bootdotdev)"
print(extract_markdown_links(link))






