from src.textnode import TextType, TextNode
from enum import Enum

class Delimiters(Enum):
    BOLD = "**"
    ITALIC = "_"
    CODE = "`"

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    if delimiter not in [d.value for d in Delimiters]:
        raise Exception("Invalid markdown syntax: unknown delimiter.")

    final_nodes = []

    for node in old_nodes:
        # Keep non-text nodes unchanged
        if node.text_type != TextType.TEXT:
            final_nodes.append(node)
            continue

        # If the delimiter isn't present, keep the node as-is
        if delimiter not in node.text:
            final_nodes.append(node)
            continue

        parts = node.text.split(delimiter)

        # Check for balanced delimiters (must result in odd number of parts)
        if len(parts) % 2 == 0:
            raise Exception("Invalid markdown syntax: missing closing delimiter.")

        # Reconstruct nodes
        for i, part in enumerate(parts):
            if i % 2 == 0:
                if part != "":
                    final_nodes.append(TextNode(part, TextType.TEXT))
            else:
                final_nodes.append(TextNode(part.strip(), text_type))

    return final_nodes


def main():
    # testing
    original_nodes =  [

                      TextNode("This is **bold** and _italic_", TextType.TEXT),
                      TextNode("This is **all of this is bold**", TextType.TEXT),
                      TextNode("This is **italic**", TextType.BOLD),
                      TextNode("This is a `code block` and its in **bold**", TextType.TEXT)
                      ]
    stuff = split_nodes_delimiter(original_nodes, "**", TextType.BOLD)
    print(stuff)



if __name__ == '__main__':
    main()







