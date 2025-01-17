

def generate_page(from_path, template_path, dest_path):
    """
    Generates a HTML page from a markdown file and a template.

    Args:
        from_path (str): The path to the markdown file.
        template_path (str): The path to the template file.
        dest_path (str): The path to the destination file.

    Returns:
        None
    """
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")