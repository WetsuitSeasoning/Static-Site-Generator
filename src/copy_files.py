import os
import shutil

def copy_files(src_dir, dest_dir):
    """
    Copy files from source directory to destination directory.

    Args:
        src_dir (str): Source directory.
        dest_dir (str): Destination directory.

    Returns:
        None
    """
    # First, check if destination directory exists
    if not os.path.exists(dest_dir):
        try:
            os.makedirs(dest_dir)
        except OSError as e:
            print(f"Error: {e}")
            return
    elif len(os.listdir(dest_dir)) > 0:
        # Delete all files in destination directory
        try:
            shutil.rmtree(dest_dir)
            os.makedirs(dest_dir)
        except Exception as e:
            print(f"Error: {e}")
            return

    # Copy files from source directory to destination directory
        