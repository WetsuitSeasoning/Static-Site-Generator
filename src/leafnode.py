from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props):
        super().__init__(tag, value, None, props)

    def to_html(self):
        VOID_TAGS = {
            "area", "base", "br", "col", "embed", "hr", "img",
            "input", "link", "meta", "source", "track", "wbr"
        }

        if self.value is None:
            raise ValueError("value cannot be empty")
        elif self.tag == None:
            return self.value
        elif self.tag in VOID_TAGS:
            return f"<{self.tag}{super().props_to_html()}>"
        else:
            return f"<{self.tag}{super().props_to_html()}>{self.value}</{self.tag}>"