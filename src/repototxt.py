# repototxt.py
from get_repo_contents import get_repo_contents

if __name__ == '__main__':
    repo_url = input("Please enter the GitHub repository URL: ")
    try:
        print(f"Getting repository contents for {repo_url}...")
        repo_name, instructions, readme_content, repo_structure, file_contents = get_repo_contents(repo_url)
        print(f"Got repository contents for {repo_url}.")
        
        # Construct the output filename path
        output_dir = "docs"
        output_filename = os.path.join(output_dir, f'{repo_name}_contents.txt')
        
        with open(output_filename, 'w', encoding='utf-8') as f:
            print(f"Writing to {output_filename}...")
            f.write(instructions)
            f.write(f"README:\n{readme_content}\n\n")
            f.write(repo_structure)
            f.write('\n\n')
            f.write(file_contents)
            print(f"Wrote to {output_filename}.")
        print(f"Repository contents saved to '{output_filename}'.")
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An error occurred: {e}")
        print("Please check the repository URL and try again.")