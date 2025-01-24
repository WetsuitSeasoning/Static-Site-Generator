import os
from copy_files import copy_files
from markdown import extract_title

dir_path = os.path.dirname(os.path.realpath(__file__))

static_path = os.path.join(os.path.dirname(dir_path), "static")
public_path = os.path.join(os.path.dirname(dir_path), "public")

def main():
    #print(f"Working Directory: {dir_path}")
    #print(f"Static Path: {static_path}")
    #print(f"Public Path: {public_path}")
    copy_files(static_path, public_path)





main()