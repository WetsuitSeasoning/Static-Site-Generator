from textnode import *

class HTMLNode:
    def __init__(self, tag: str=None, value: str=None, children: list=None, props: dict=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError()
    
    def props_to_html(self):
        props_string = ""
        if self.props == None:
            return props_string
        for key in self.props:
            value = self.props[key]
            props_string += f" {key}=\"{value}\""
        return props_string

    def __repr__(self):
        return f"tag= {self.tag}, value= {self.value}, children= {self.children}, props= {self.props}"