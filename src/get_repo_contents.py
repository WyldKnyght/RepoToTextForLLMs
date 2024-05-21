# get_repo_contents.py
import os
from dotenv import load_dotenv
from urllib.parse import urlparse
from github import Github
from get_readme_content import get_readme_content
from traverse_repo_iteratively import traverse_repo_iteratively
from get_file_contents_iteratively import get_file_contents_iteratively
from utils.create_instructions import create_instructions

load_dotenv()

GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')

def get_repo_contents(repo_url):
    """
    Main function to get repository contents.
    """
    parsed_url = urlparse(repo_url)
    repo_name = parsed_url.path.split('/')[-1]
    if not GITHUB_TOKEN:
        raise ValueError("Please set the 'GITHUB_TOKEN' environment variable.")
    print(f"Getting Github object with token: {GITHUB_TOKEN}")
    g = Github(GITHUB_TOKEN)
    print(f"Getting repository object for: {repo_name}")
    repo = g.get_repo(parsed_url.path[1:])

    activity = f"Fetching details for: {repo_name}"
    print(f"{activity}\n{'-' * len(activity)}")
    print(f"Getting README content for: {repo_name}")
    readme_content = get_readme_content(repo)
    print(f"Getting repository structure for: {repo_name}")
    repo_structure = (
        f"Repository Structure: {repo_name}\n{traverse_repo_iteratively(repo)}"
    )
    print(f"Getting file contents for: {repo_name}")
    file_contents = get_file_contents_iteratively(repo)
    print(f"Generating instructions for: {repo_name}")
    instructions = create_instructions(repo_name)

    return repo_name, instructions, readme_content, repo_structure, file_contents


