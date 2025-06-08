from htmlnode import HTMLNode
from leafnode import LeafNode
from parentnode import ParentNode
from textnode import TextNode
from textnode import TextType


def main():
    child_node = LeafNode("child", "span")
    parent_node = ParentNode("div", [child_node])
    print(parent_node.to_html())

    print(parent_node.to_html() == "<div><span>child</span></div>")

    new_node = ParentNode(
    "p",
    [
        LeafNode("Bold text", "b"),
        LeafNode("Normal text", None),
        LeafNode("Italic text", "i"),
        LeafNode("Normal text", None)
    ],
)

    print(new_node.to_html())

    grandchild = LeafNode("grandchild text", "b")
    child = ParentNode("span", [grandchild])
    parent = ParentNode("div", [child])

    print(parent.to_html())







if __name__ == "__main__":
    main()
    
