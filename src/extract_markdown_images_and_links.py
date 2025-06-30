import re
from textnode import TextNode
from textnode import TextType

# returns a list of alt text and an image
def extract_markdown_images(markdown_text):
    list_of_tuples = re.findall(r"!\[(.*?)\]\((.*?)\)", markdown_text)
    return list_of_tuples

# returns alt text and link
def extract_markdown_links(markdown_text):
    list_of_tuples = re.findall(r"(?<!!)\[(.*?)\]\((.*?)\)", markdown_text)
    return list_of_tuples

def split_nodes_image(old_nodes):
    new_nodes = []

    for node in old_nodes:
        # Only process TextNodes of type TEXT
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        text = node.text
        images = extract_markdown_images(text)

        # If no images, keep the node as-is
        if not images:
            new_nodes.append(node)
            continue

        for alt, url in images:
            # Split the text once on the current image
            split_text = text.split(f"![{alt}]({url})", 1)
            before = split_text[0]
            after = split_text[1]

            # Add text before the image if it's not empty
            if before:
                new_nodes.append(TextNode(before, TextType.TEXT))

            # Add the image node
            new_nodes.append(TextNode(alt, TextType.IMAGE, url))

            # Continue processing the rest of the text
            text = after

        # After all images are processed, there may be leftover text
        if text:
            new_nodes.append(TextNode(text, TextType.TEXT))

    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        text = node.text
        links = extract_markdown_links(text)

        if not links:
            new_nodes.append(node)
            continue

        for alt, url in links:
            split_text = text.split(f"[{alt}]({url})", 1)
            before = split_text[0]
            after = split_text[1]

            if before:
                new_nodes.append(TextNode(before, TextType.TEXT))

            new_nodes.append(TextNode(alt, TextType.LINK, url))

            text = after

        if text:
            new_nodes.append(TextNode(text, TextType.TEXT))

    return new_nodes












