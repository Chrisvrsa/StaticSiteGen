class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        # child classes will override this method
        raise NotImplementedError()

    def props_to_html(self):
        if self.props is None:
            return ""
        key_and_value_lst = []

        # .items returns a list of key value tuples
        for key, value in self.props.items():
            key_and_value_lst.append(f' {key}="{value}"')

        return "".join(key_and_value_lst)

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"
