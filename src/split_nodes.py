from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes: list[TextNode], delimiter, text_type) -> list[TextNode]:
    """
    Splits the given list of TextNode objects by the specified delimiter.

    Args:
        old_nodes (list[TextNode]): The list of TextNode objects to split.
        delimiter (str): The delimiter to split the text of the TextNode objects.
        text_type (TextType): The text type to assign to the new nodes created from the delimiter.

    Returns:
        list[TextNode]: A new list of TextNode objects split by the delimiter.
    """
    new_nodes = []
    for node in old_nodes:
        if not isinstance(node.text_type, TextType):
            raise ValueError(f"node text type {node.text_type} is not an instance of TextType")
        if node.text_type == TextType.TEXT:
            if node.text.count(delimiter) % 2:
                raise ValueError(f"delimiter {delimiter} count is not even in node text {node.text}")
            
            parts = node.text.split(delimiter)
            for i in range(0, len(parts), 2):
                new_nodes.append(TextNode(parts[i], node.text_type, node.url))
                if i + 1 < len(parts):
                    new_nodes.append(TextNode(parts[i + 1], text_type, node.url))
            
        else:
            new_nodes.append(node)

    return new_nodes