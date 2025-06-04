from public.src.htmlnode import HTMLNode
from textnode import TextNode
from textnode import TextType

def main():
    new_html_node = HTMLNode("101", "New HTML node", None, {"href": "https://www.google.com", "target": "_blank"})
    # This will print the object details
    print(new_html_node)
    print("Method test: " + "\n" + new_html_node.props_to_html())


if __name__ == "__main__":
    main()
    
