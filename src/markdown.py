

def extract_title(markdown: str) -> str:
    """
    Pulls the h1 header from a markdown string.

    Args:
        markdown: A markdown string.

    Returns:
        The title of the markdown string.
    """
    if not markdown.startswith("# "):
        raise ValueError("No title found in markdown string")

    