

class HTMLNode:

    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def __repr__(self):
        return f"HTMLNode(tag={self.tag}, value={self.value}, children={self.children}, props={self.props})"

    def to_html(self):
        raise NotImplementedError("Soon TM")
    
    def props_to_html(self):
        if not self.props:
            return ""
        return " " + " ".join(f'{key}="{value}"' for key, value in self.props.items())


class LeafNode(HTMLNode):

    def __init__(self, tag, value, props=None):
        super().__init__(tag=tag, value=value, props=props)
        self.children = None

    def to_html(self):
        if not self.value:
            raise ValueError("LeafNode must have a value to convert to HTML")
        if not self.tag:
            return self.value
        props_html = self.props_to_html()
        return f"<{self.tag}{props_html}>{self.value}</{self.tag}>"
    

class ParentNode(HTMLNode):

    def __init__(self, tag, children, props=None):
        super().__init__(tag=tag, children=children, props=props)
        self.value = None

    def to_html(self):
        if not self.tag:
            raise ValueError("ParentNode must have a tag to convert to HTML")
        if not self.children:
            raise ValueError("ParentNode must have children")
        props_html = self.props_to_html()
        children_html = "".join(child.to_html() for child in self.children)
        return f"<{self.tag}{props_html}>{children_html}</{self.tag}>"
    