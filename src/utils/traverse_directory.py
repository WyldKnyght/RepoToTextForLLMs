# utils/traverse_directory.py
import os
from tqdm import tqdm
from utils.process_file import process_file

def traverse_directory(path, contents, binary_extensions, visited, repo):
    file_contents = ""
    visited.add(path)
    for content in tqdm(contents, desc=f"Downloading {path}", leave=False):
        if content.type == "dir" and content.path not in visited:
            file_contents += traverse_directory(os.path.join(path, content.name), repo.get_contents(content.path), binary_extensions, visited, repo)
        else:
            file_contents += process_file(content, path, binary_extensions)
    return file_contents