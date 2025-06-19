import os
import logging
import shutil
from git import Repo, GitCommandError
from dotenv import load_dotenv

# Load GitHub token from .env
load_dotenv()
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
if not GITHUB_TOKEN:
    raise ValueError("GITHUB_TOKEN not found in .env file.")

# Configuration
REPO_DIR = "dummy_git_repo"
BRANCH_NAME = "feature-branch"
GITHUB_USERNAME = "DRgit03"
GITHUB_REPO_NAME = "dummy_git_repo"
GITHUB_REPO_URL = f"https://{GITHUB_USERNAME}:{GITHUB_TOKEN}@github.com/{GITHUB_USERNAME}/{GITHUB_REPO_NAME}.git"

# Setup logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

try:
    # Initialize or load Git repo
    if not os.path.exists(REPO_DIR):
        os.makedirs(REPO_DIR)
        repo = Repo.init(REPO_DIR)
        logging.info("Initialized new Git repo.")
    else:
        repo = Repo(REPO_DIR)
        logging.info("Loaded existing Git repo.")

    # Change to the repo directory
    os.chdir(REPO_DIR)

    # Create and checkout feature branch
    if BRANCH_NAME not in repo.heads:
        repo.create_head(BRANCH_NAME)
        logging.info(f"Created branch: {BRANCH_NAME}")
    repo.head.reference = repo.heads[BRANCH_NAME]
    repo.head.reset(index=True, working_tree=True)
    logging.info(f"Switched to branch: {BRANCH_NAME}")

    # Create dummy file
    dummy_file = "dummy_feature.txt"
    with open(dummy_file, "w") as f:
        f.write("This is a test file created on a feature branch using GitPython test check.\n")
    logging.info(f"Created file: {dummy_file}")

    files_to_add = [dummy_file]

    # Copy the Python script into the repo (from parent)
    script_name = "git_python_test.py"
    script_src = os.path.join("..", script_name)
    if os.path.exists(script_src):
        shutil.copy(script_src, script_name)
        logging.info(f"Copied {script_name} into Git repo.")
        files_to_add.append(script_name)

    # Copy README.md from parent folder if exists
    readme_name = "README.md"
    readme_src = os.path.join("..", readme_name)
    if os.path.exists(readme_src):
        shutil.copy(readme_src, readme_name)
        logging.info("Copied README.md into Git repo.")
        files_to_add.append(readme_name)

    # Stage and commit
    repo.index.add(files_to_add)
    repo.index.commit("Add dummy file, script, and README")
    logging.info("Committed all files.")

    # Log commit history
    logging.info("Commit history:")
    for commit in repo.iter_commits():
        logging.info(f"{commit.hexsha[:7]} - {commit.author.name}: {commit.message.strip()}")

    # Add remote if not present
    if "origin" not in [remote.name for remote in repo.remotes]:
        repo.create_remote("origin", url=GITHUB_REPO_URL)
        logging.info("Added GitHub remote.")

    # Push branch
    repo.remote("origin").push(refspec=f"{BRANCH_NAME}:{BRANCH_NAME}")
    logging.info(f"Pushed branch '{BRANCH_NAME}' to GitHub.")

except GitCommandError as git_err:
    logging.error(f"Git error: {git_err}")
except Exception as e:
    logging.error(f"Unexpected error: {e}")
