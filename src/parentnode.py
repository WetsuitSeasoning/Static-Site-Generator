from htmlnode import *

class ParentNode(HTMLNode):
    def __init__(self, tag, children: list[HTMLNode], props: dict=None):
        if children == None or children == []:
            raise ValueError("children cannot be empty or None")
        if tag == None:
            raise ValueError("tag cannot be empty")
        
        super().__init__(tag, None, children, props)

    def to_html(self):
        output_string = ""
        #if len(self.children) == 0:
            #raise ValueError("Parent node must have children")
        for child in self.children:
            if not isinstance(child, HTMLNode):
                raise ValueError(f"child {child} is not an instance of HTMLNode")
            output_string += child.to_html()

        return f"<{self.tag}{super().props_to_html()}>{output_string}</{self.tag}>"
