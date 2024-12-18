from enum import Enum

class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode:
    def __init__(self, text, text_type: TextType, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, obj):
        #check if obj is an instance of the TextNode class before checking for matching attributes
        if not isinstance(obj, TextNode):
            raise Exception(f"{obj} is not an instance of TextNode")
        
        #check for matching attributes. True if all match, False otherwise
        return self.text == obj.text and self.text_type == obj.text_type and self.url == obj.url
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"