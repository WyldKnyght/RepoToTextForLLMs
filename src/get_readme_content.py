# get_readme_content.py

def get_readme_content(repo):
    """
    Retrieve the content of the README file.
    """
    try:
        readme = repo.get_contents("README.md")
        return readme.decoded_content.decode('utf-8')
    except FileNotFoundError:
        return "README not found."
