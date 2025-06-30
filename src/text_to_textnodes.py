
from textnode import TextNode, TextType
from split_nodes_delimiter import split_nodes_delimiter
from extract_markdown_images_and_links import split_nodes_image, split_nodes_link

def text_to_textnodes(raw_markdown_text):
    nodes = [TextNode(raw_markdown_text, TextType.TEXT)]

    # Split image and link markdown first
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)

    # Then split bold, italic, and code
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)

    return nodes



