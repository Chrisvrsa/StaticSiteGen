from htmlnode import HTMLNode
from leafnode import LeafNode


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag=tag, value=None, children=children, props=props)

    def to_html(self):
        if self.tag == None:
            raise ValueError('ParentNode must have a tag.')
        if not self.children:
            raise ValueError('Argument "children" cannot be None.')
        
        list_of_children = []
        
        for child in self.children:
            list_of_children.append(child.to_html())
            
        final_string = "".join(list_of_children)
        
        return f"<{self.tag}>{final_string}</{self.tag}>"
