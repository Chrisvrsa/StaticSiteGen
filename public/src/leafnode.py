from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, value, tag=None, props=None):
        if value is None:
            raise ValueError("Value must not be None")
        super().__init__(tag=tag, value=value, props=props, children=None)

        # self note, is is for object identity. == is for equal values

    def to_html(self):
        
        if self.tag is None:
            return self.value
        else:
            return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
            

        