from textnode import TextNode, TextType
from leafnode import LeafNode

def text_node_to_html_node(text_node: TextNode):
    if not isinstance(text_node, TextNode):
        raise ValueError("argument must be an instance of TextNode")
    
    match text_node.text_type:
        case TextType.TEXT:
            node = LeafNode(None, text_node.text, None)
        case TextType.BOLD:
            node = LeafNode("b", text_node.text, None)
        case TextType.ITALIC:
            node = LeafNode("i", text_node.text, None)
        case TextType.CODE:
            node = LeafNode("code", text_node.text, None)
        case TextType.LINK:
            props = {"href": text_node.url}
            node = LeafNode("a", text_node.text, props)
        case TextType.IMAGE:
            props = {"src": text_node.url, "alt": text_node.text}
            node = LeafNode("img", "", props)
        case _:
            raise ValueError(f"unexpected TextType {text_node.text_type}")

    return node