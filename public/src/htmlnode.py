class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        # Child classes will overwrite this method to render HTML
        raise NotImplementedError()

    def props_to_html(self):
        items = []

        if self.props is None:
            return f""
        for key, value in self.props.items():
            items.append(f' {key}=\"{value}\"')

        return ''.join(items)


    def __repr__(self):
        return f"{self.tag} {self.value}, {self.children}, {self.props}"






