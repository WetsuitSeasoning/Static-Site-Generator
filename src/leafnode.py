from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag: str, value: str, props: dict):
        if value is None:
            raise ValueError("value cannot be None")
        super().__init__(tag, value, None, props) #LeafNode tags cannot have children
        
    VOID_TAGS = {
        "area", "base", "br", "col", "embed", "hr", "img",
        "input", "link", "meta", "source", "track", "wbr"
    }

    def to_html(self):
        if self.tag is None:
            return self.value
        elif self.tag in self.VOID_TAGS:
            return f"<{self.tag}{self.props_to_html()}>"
        else:
            return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"