import os
import json
from github import Github

def generate_json(folder_path, repo_name, branch_name):
    icons = []
    folder_name = os.path.basename(folder_path)
    
    for filename in os.listdir(folder_path):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
            icon_url = f"https://github.com/{repo_name}/raw/{branch_name}/{folder_path}/{filename}"
            icons.append({
                "name": os.path.splitext(filename)[0],
                "url": icon_url
            })
    
    return {
        "name": f"WHATSINStach {folder_name.capitalize()}",
        "description": f"{folder_name.capitalize()} iconset",
        "icons": icons
    }

# Get repository information
g = Github(os.environ['GITHUB_TOKEN'])
repo = g.get_repo(os.environ['GITHUB_REPOSITORY'])
branch = repo.get_branch(os.environ['GITHUB_REF'].split('/')[-1])

# Specify the main folder to scan
main_folder = 'iconset'

# Generate JSON for each subfolder
for subfolder in os.listdir(main_folder):
    subfolder_path = os.path.join(main_folder, subfolder)
    if os.path.isdir(subfolder_path):
        json_data = generate_json(subfolder_path, repo.full_name, branch.name)
        
        # Write JSON file with subfolder name
        json_filename = f"{subfolder}.json"
        with open(os.path.join(main_folder, json_filename), 'w') as f:
            json.dump(json_data, f, indent=4)

print("JSON files generated successfully.")
