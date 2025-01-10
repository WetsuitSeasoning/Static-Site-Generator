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
    try:
        for root, dirs, files in os.walk(src_dir):
            # Create corresponding directories in destination
            for dir in dirs:
                dest_path = os.path.join(dest_dir, os.path.relpath(os.path.join(root, dir), src_dir))
                if not os.path.exists(dest_path):
                    os.makedirs(dest_path)
            # Copy files
            for file in files:
                src_file_path = os.path.join(root, file)
                dest_file_path = os.path.join(dest_dir, os.path.relpath(src_file_path, src_dir))
                #print(f"Copying {src_file_path} to {dest_file_path}")
                shutil.copy2(src_file_path, dest_file_path)
    except Exception as e:
        print(f"Error: {e}")
        return
        