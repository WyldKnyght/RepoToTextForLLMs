# traverse_repo_iteratively.py
from tqdm import tqdm

def traverse_repo_iteratively(repo):
    """
    Traverse the repository iteratively to avoid recursion limits for large repositories.
    """
    structure = ""
    dirs_to_visit = [("", repo.get_contents(""))]
    dirs_visited = set()

    for path, contents in tqdm(dirs_to_visit, desc="Processing directories", leave=False):
        dirs_visited.add(path)
        for content in contents:
            if content.type == "dir":
                if content.path not in dirs_visited:
                    structure += f"{path}/{content.name}/\n"
                    dirs_to_visit.append((f"{path}/{content.name}", repo.get_contents(content.path)))
            else:
                structure += f"{path}/{content.name}\n"
    return structure
