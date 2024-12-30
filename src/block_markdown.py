

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