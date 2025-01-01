from enum import Enum
from htmlnode import HTMLNode
from parentnode import ParentNode
from leafnode import LeafNode
from inline_markdown import text_to_textnodes
from textnode_to_htmlnode import text_node_to_html_node
import re

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def markdown_to_blocks(markdown: str) -> list[str]:
    """
    Convert markdown text to a list of blocks
    
    Args:
        markdown (str): markdown text

    Returns:
        blocks: list of strings representing blocks
    """
    blocks = [] # Start an empty list of blocks

    blocks = markdown.split("\n\n") # Split the markdown text into blocks. We look for two newlines to separate blocks

    blocks = list(filter(lambda block: block != "", blocks)) # Remove empty blocks
    blocks = [block.strip() for block in blocks] # Remove leading and trailing whitespaces from blocks
    
    return blocks

def block_to_blocktype(block: str) -> str:
    """
    Determine the type of block
    
    Args:
        block (str): A string representing a block
    
    Returns:
        block_type: A string representing the type of block        
    """
    if block.startswith("#"):
        return BlockType.HEADING.value # The block starts with 1 or more # characters, representing a heading
    elif block.startswith("```") and block.endswith("```"):
        return BlockType.CODE.value # The block starts and ends with 3 backticks, representing code
    elif all(line.startswith(">") for line in block.split("\n")):
        return BlockType.QUOTE.value # All lines in the block start with >, representing a quote
    elif all(line.lstrip().startswith("* ") for line in block.split("\n")):
        return BlockType.UNORDERED_LIST.value # All lines in the block start with *, representing an unordered list
    elif all(line.lstrip().startswith("- ") for line in block.split("\n")):
        return BlockType.UNORDERED_LIST.value # All lines in the block start with -, representing an unordered list
    elif all(line.lstrip().startswith("+ ") for line in block.split("\n")):
        return BlockType.UNORDERED_LIST.value # All lines in the block start with +, representing an unordered list
    elif all(re.match(r'^\d+\.\s', line.lstrip()) for line in block.split("\n")):
        return BlockType.ORDERED_LIST.value # All lines in the block start with 1., 2., 3., etc., representing an ordered list
    else:
        return BlockType.PARAGRAPH.value # None of the above, return paragraph
    
def markdown_to_html_node(markdown: str) -> ParentNode:
    """
    Convert markdown text to a tree of HTML nodes
    
    Args:
        markdown (str): markdown text

    Returns:
        node: A ParentNode representing the root of the HTML tree, with nested HTML nodes representing the markdown text
    """
    blocks = markdown_to_blocks(markdown) # Convert markdown text to blocks

    child_nodes = [] # Start an empty list of child nodes

    for block in blocks:
        block_type = block_to_blocktype(block) # Determine the type of block
        match block_type:
            case "paragraph":
                tag = "p"
                children = text_to_children(block) # Convert the block to a list of HTML nodes
                child_nodes.append(ParentNode(tag, children, None))
            case "heading":
                header_level = get_header_level(block) # Get the level of the header
                tag = f"h{header_level}"
                children = text_to_children(clean_header_text(block)) # Convert the block to a list of HTML nodes
                child_nodes.append(ParentNode(tag, children, None))
            case "code":
                inner_tag = "code"
                text_node = LeafNode(None, clean_code_text(block), None) # Create a LeafNode object with the cleaned code text
                inner_node = ParentNode(inner_tag, [text_node], None) # Create a parent node with the HTML node as a child
                outer_tag = "pre"
                child_nodes.append(ParentNode(outer_tag, [inner_node], None))
            case "quote":
                tag = "blockquote"
                quote_text = clean_quote_text(block) # Clean the quote text
                children = text_to_children(quote_text) # Convert the block to a list of HTML nodes
                child_nodes.append(ParentNode(tag, children, None))
            case "unordered_list":
                list_items = block.split("\n") # Split the block into list items
                processed_items = [process_unordered_list_item(item) for item in list_items] # Process each list item
                root_node = build_list_structure(processed_items, "ul") # Build a nested list structure
                child_nodes.append(root_node) # Append the root node to the list of HTML nodes

            case "ordered_list":
                list_items = block.split("\n")
                processed_items = [process_ordered_list_item(item) for item in list_items] # Process each list item
                root_node = build_list_structure(processed_items, "ol") # Build a nested list structure
                child_nodes.append(root_node) # Append the root node to the list of HTML nodes

    return ParentNode("div", child_nodes, None)


def text_to_children(text:str) -> list[HTMLNode]:
    """
    Convert text to a list of HTML nodes
    
    Args:
        text (str): text

    Returns:
        nodes: list of HTML nodes
    """
    nodes = [] # Start an empty list of nodes

    text_nodes = text_to_textnodes(text) # Convert input text to a list of TextNode objects

    for text_node in text_nodes:
        node = text_node_to_html_node(text_node) # Convert each TextNode object to an HTML node
        nodes.append(node) # Append the HTML node to the list of nodes

    return nodes

def get_header_level(block: str) -> int:
    """
    Get the level of the header
    
    Args:
        block (str): A string representing a block, beginning with one or more '#' characters

    Returns:
        level: An integer representing the level of the header
    """
    level = 0 # Start with a header level of 0

    for char in block:
        if char == "#":
            level += 1
        else:
            break

    if level > 6:
        raise ValueError("Header level cannot be greater than 6")
    elif level == 0:
        raise ValueError("Header level cannot be 0")
    else:
        return level
    
def clean_header_text(block: str) -> str:
    """
    Remove leading '#' characters, and leading/trailing whitespace from a header block
    
    Args:
        block (str): A string representing a header block
    
    Returns:
        text: A string representing the cleaned header text
    """
    text = block.lstrip("#") # Remove leading '#' characters
    text = text.strip() # Remove leading and trailing whitespace

    return text

def clean_code_text(block: str) -> str:
    """
    Remove leading '```' characters, and leading/trailing whitespace from a code block
    
    Args:
        block (str): A string representing a code block
    
    Returns:
        text: A string representing the cleaned code text
    """
    text = block.strip("```") # Remove leading and trailing '```' characters
    text = text.strip("\n") # Remove leading and trailing newlines
    text = text.strip() # Remove leading and trailing whitespace

    return text

def clean_quote_text(block: str) -> str:
    """
    Remove leading '>' characters, and leading/trailing whitespace from a quote block
    
    Args:
        block (str): A string representing a quote block
    
    Returns:
        text: A string representing the cleaned quote text
    """
    lines = block.split("\n") # Split the block into lines
    cleaned_lines = []
    for line in lines:
        cleaned_line = line.lstrip(">").strip() # Remove leading '>' characters and leading/trailing whitespace
        cleaned_lines.append(cleaned_line)

    return "\n".join(cleaned_lines) # Join the cleaned lines into a single string

def clean_unordered_list_item(block: str) -> str:
    """
    Remove leading '*', '-', and '+' characters, and leading/trailing whitespace from a list item block
    
    Args:
        block (str): A string representing a list item block
    
    Returns:
        text: A string representing the cleaned list item text
    """
     # First strip whitespace
    text = block.lstrip()
    
    # Then check if it starts with a list marker
    if text.startswith(('* ', '- ', '+ ')):
        text = text[2:]  # Remove the marker and the space after it
        
    return text.strip()

def clean_ordered_list_item(block: str) -> str:
    """
    Remove leading '1.', '2.', '3.', etc., characters, and leading/trailing whitespace from a list item block
    
    Args:
        block (str): A string representing a list item block
    
    Returns:
        text: A string representing the cleaned list item text
    """
    text = block.split(".", 1)[1] # Remove leading '1.', '2.', '3.', etc., characters
    text = text.strip() # Remove leading and trailing whitespace

    return text

def process_unordered_list_item(line: str) -> tuple[str, int]:
    """
    Process a list item line, returning its cleaned text and indent level.

    Args:
        line (str): A string representing a list item line like '    * Nested item'

    Returns:
        tuple of (cleaned_text, indent_level)
    """
    leading_spaces = len(line) - len(line.lstrip()) # Calculate the number of leading spaces
    indent = leading_spaces // 2 # Calculate the indent level
    cleaned = clean_unordered_list_item(line) # Clean the list item text
    return cleaned, indent

def process_ordered_list_item(line: str) -> tuple[str, int]:
    """
    Process a list item line, returning its cleaned text and indent level.

    Args:
        line (str): A string representing a list item line like '    1 Nested item'

    Returns:
        tuple of (cleaned_text, indent_level)
    """
    leading_spaces = len(line) - len(line.lstrip()) # Calculate the number of leading spaces
    indent = leading_spaces // 2 # Calculate the indent level
    cleaned = clean_ordered_list_item(line) # Clean the list item text
    return cleaned, indent

def build_list_structure(processed_items: list[tuple[str, int]], list_tag: str="ul") -> ParentNode:
    """
    Build a nested list structure from a list of processed list items.

    Args:
        processed_items (list): A list of tuples containing cleaned text and indent level
        list_tag (str): The tag to use for the outer list (default is 'ul')

    Returns:
        root_node: A ParentNode representing the root of the nested list structure
    """
    if not processed_items:
        return None

    nodes_list = []
    for text, indent_level in processed_items:
        nodes_list.append((ParentNode("li", text_to_children(text), None), indent_level))

    root_node, _ = process_at_level(nodes_list, 0, 0, list_tag)

    return root_node

def process_at_level(nodes_list: list[tuple[ParentNode, int]], start_index: int, current_indent: int, list_tag: str="ul") -> tuple[ParentNode, int]:
    """
    Recursively process a list of nodes at a given indentation level.

    Args:
        nodes_list (list): A list of tuples containing nodes and their indentation levels
        start_index (int): The index to start processing from
        current_indent (int): The current indentation level
        list_tag (str): The tag to use for the outer list (default is 'ul')

    Returns:
        tuple of (parent_node, next_index)
    """
    # Base case
    if start_index >= len(nodes_list):
        return None, start_index
    
    # Also stop if we find a node with less indentation
    current_node, indent = nodes_list[start_index]
    if indent < current_indent:
        return None, start_index

    # Start collecting nodes at this level
    nodes_at_level = [current_node]
    next_index = start_index + 1

    # Check next node
    while next_index < len(nodes_list):
        next_node, next_indent = nodes_list[next_index]
        if next_indent == current_indent: # If the next node has the same indentation, add it to the list of nodes at the current level
            nodes_at_level.append(next_node)
            next_index += 1
        elif next_indent > current_indent:
            # Recurse to process the next level
            nested_nodes, next_index = process_at_level(nodes_list, next_index, next_indent, list_tag)
            if nested_nodes is not None:
                last_node = nodes_at_level[-1]
                last_node.children.append(nested_nodes)
        else: # If the next node has less indentation, stop
            break

    parent_node = ParentNode(list_tag, nodes_at_level, None)
    return parent_node, next_index