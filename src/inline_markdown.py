import re
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

def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
    """
    Splits the given list of TextNode objects by images.

    Args:
        old_nodes (list[TextNode]): The list of TextNode objects to split.

    Returns:
        list[TextNode]: A new list of TextNode objects split by images.
    """
    new_nodes = []
    for node in old_nodes:
        if not isinstance(node.text_type, TextType):
            raise ValueError(f"node text type {node.text_type} is not an instance of TextType")
        
        if node.text_type == TextType.TEXT:
            image_text = extract_markdown_images(node.text)
            node_text = node.text
            
            if len(image_text) > 0: # At least 1 image was found in the node
                for alt_text, image_url in image_text:
                    split_text = node_text.split(f"![{alt_text}]({image_url})", maxsplit=1)
                    
                    if split_text[0] != "": # There is text before the image
                        new_nodes.append(TextNode(split_text[0], TextType.TEXT))
                    
                    new_nodes.append(TextNode(alt_text, TextType.IMAGE, image_url))
                    
                    node_text = split_text[1] if len(split_text) > 1 else ""
                
                if node_text != "": # There is text after the last image
                    new_nodes.append(TextNode(node_text, TextType.TEXT))

            else: # No image was found in the node
                new_nodes.append(node)
        
        else: # The node is not text
            new_nodes.append(node)

    return new_nodes

def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
    """
    Splits the given list of TextNode objects by links.

    Args:
        old_nodes (list[TextNode]): The list of TextNode objects to split.
    
    Returns:
        list[TextNode]: A new list of TextNode objects split by links.
    """
    new_nodes = []
    for node in old_nodes:
        if not isinstance(node.text_type, TextType):
            raise ValueError(f"node text type {node.text_type} is not an instance of TextType")
        
        if node.text_type == TextType.TEXT:
            link_text = extract_markdown_links(node.text)
            node_text = node.text
            
            if len(link_text) > 0: # At least 1 link was found in the node
                for link_words, link_url in link_text:
                    split_text = node_text.split(f"[{link_words}]({link_url})", maxsplit=1)
                    
                    if split_text[0] != "": # There is text before the link
                        new_nodes.append(TextNode(split_text[0], TextType.TEXT))

                    new_nodes.append(TextNode(link_words, TextType.LINK, link_url))

                    node_text = split_text[1] if len(split_text) > 1 else ""

                if node_text != "": # There is text after the last link
                    new_nodes.append(TextNode(node_text, TextType.TEXT))

            else: # No link was found in the node
                new_nodes.append(node)

        else: # The node is not text
            new_nodes.append(node)
    
    return new_nodes

def extract_markdown_images(text: str) -> list[tuple]:
    """
    Extracts image URLs from the given text.

    Args:
        text (str): The text to extract image URLs from.

    Returns:
        list[tuple]: A list of tuples containing the image URLs and their alt text.
    """
    pattern = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(pattern, text)
    return matches

def extract_markdown_links(text: str) -> list[tuple]:
    """
    Extracts link URLs from the given text.

    Args:
        text (str): The text to extract link URLs from.

    Returns:
        list[tuple]: A list of tuples containing the link URLs and their link text.
    """
    pattern = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(pattern, text)
    return matches