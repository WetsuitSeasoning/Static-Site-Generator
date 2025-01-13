

def extract_title(markdown: str) -> str:
    """
    Pulls the h1 header from a markdown string, and strips the leading '#' and any leading/trailing whitespace.

    Args:
        markdown: A markdown string.

    Returns:
        The title of the markdown string.
    """
    if not markdown.startswith("# "):
        raise ValueError("No title found in markdown string")

    return markdown[2:].split("\n", 1)[0].strip()