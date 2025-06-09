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

# self note, as someone coming from other languages. __name__ == "__main__" means that this files should be run 
# when purposley running the file, it should not be run if its imported to another file. Every file in python 
# automatically has a name variable
if __name__ == "__main__":
    main()
    
