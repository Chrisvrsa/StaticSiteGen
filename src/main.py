from textnode import TextNode
from leafnode import LeafNode
from parent_node import ParentNode
from textnode import TextType


def main():
    textnode = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
    print(textnode)

    # test_files recursive function .to_html
    node = ParentNode(
        "p",
        [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text"),
        ],
    )

    print(node.to_html())

    # test_files text_node_to_html_node function



if __name__ == "__main__":
    main()