# get_file_contents_iteratively.py
from utils.load_binary_extensions import load_binary_extensions
from utils.traverse_directory import traverse_directory

def get_file_contents_iteratively(repo, extensions_file="src/config/binary_extensions.txt"):
    binary_extensions = load_binary_extensions(extensions_file)
    return traverse_directory("", repo.get_contents(""), binary_extensions, set(), repo)
