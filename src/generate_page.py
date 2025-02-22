

def generate_page(from_path, template_path, dest_path):
    """
    Generates a HTML page from a markdown file and a template. The generated file is saved to the destination path.

    Args:
        from_path (str): The path to the markdown file.
        template_path (str): The path to the template file.
        dest_path (str): The path to the destination file.

    Returns:
        None
    """
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    with open(from_path, "r") as md_file:
        content = md_file.read() # Read in the markdown content