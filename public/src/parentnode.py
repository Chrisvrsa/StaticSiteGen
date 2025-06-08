from htmlnode import HTMLNode


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        if tag is None:
            raise ValueError('ParentNode must have a tag.')
        # you could use if children is None here, however, this is more robust.
        # not checks everything, including falsy values and an empty list if passed
        if not children:
            raise ValueError('children cannot be None')
        super().__init__(tag=tag, value=None, children=children, props=props)

    def to_html(self):
        pass

