from enum import Enum

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
    elif all(line.startswith("* ") for line in block.split("\n")):
        return BlockType.UNORDERED_LIST.value # All lines in the block start with *, representing an unordered list
    elif all(line.startswith("- ") for line in block.split("\n")):
        return BlockType.UNORDERED_LIST.value # All lines in the block start with -, representing an unordered list
    elif all(line.startswith(f"{i+1}.") for i, line in enumerate(block.split("\n"))):
        return BlockType.ORDERED_LIST.value # All lines in the block start with 1., 2., 3., etc., representing an ordered list
    else:
        return BlockType.PARAGRAPH.value # None of the above, return paragraph