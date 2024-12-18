from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children: list[HTMLNode], props: dict=None):
        if props is None:
            props = {}
        if not children: # Check for None or empty list
            raise ValueError("children cannot be empty or None")
        for child in children:
            if not isinstance(child, HTMLNode):
                raise ValueError(f"child {child} is not an instance of HTMLNode")
        if tag is None:
            raise ValueError("tag cannot be None")
        
        super().__init__(tag, None, children, props)

    def to_html(self):
        output_string = ""
        for child in self.children:
            if not isinstance(child, HTMLNode):
                raise ValueError(f"child {child} is not an instance of HTMLNode")
            output_string += child.to_html()

        return f"<{self.tag}{self.props_to_html()}>{output_string}</{self.tag}>"
