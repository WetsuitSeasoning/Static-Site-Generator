class HTMLNode:
    def __init__(self, tag: str=None, value: str=None, children: list=None, props: dict=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        """
        Convert the node to an HTML string.
        
        This method should be implemented by subclasses.
        Raises:
            NotImplementedError: If the method is not implemented by a subclass.
        """
        raise NotImplementedError()
    
    def props_to_html(self):
        props_string = ""
        if self.props is None:
            return props_string
        for key in self.props:
            value = self.props[key]
            props_string += f" {key}=\"{value}\""
        return props_string

    def __repr__(self):
        return f"tag= {self.tag}, value= {self.value}, children= {self.children}, props= {self.props}"