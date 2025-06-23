from htmlnode import HTMLNode


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        self.tag = tag
        self.children = children
        self.props = props
        super().__init__(tag=tag, value=None, children=children, props=props)

    def to_html(self):
        list_of_children = []

        if self.tag is None:
            raise ValueError("Tag cannot be None.")
        if self.children is None:
            raise ValueError("Children cannot be None.")

        for child in self.children:
            list_of_children.append(child.to_html())

        return f'<{self.tag}{self.props_to_html()}>{"".join(list_of_children)}</{self.tag}>'



