import os
import logging
import shutil
from git import Repo, GitCommandError
from dotenv import load_dotenv

# Load .env and GitHub token
load_dotenv()
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
if not GITHUB_TOKEN:
    raise ValueError(" GITHUB_TOKEN not found in .env file")

# Config
REPO_DIR = "dummy_git_repo"
BRANCH_NAME = "feature-branch"
GITHUB_USERNAME = "DRgit03"
GITHUB_REPO_NAME = "dummy_git_repo"
GITHUB_REPO_URL = f"https://{GITHUB_USERNAME}:{GITHUB_TOKEN}@github.com/{GITHUB_USERNAME}/{GITHUB_REPO_NAME}.git"

# Setup logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

try:
    # Create or load repo
    if not os.path.exists(REPO_DIR):
        os.makedirs(REPO_DIR)
        repo = Repo.init(REPO_DIR)
        logging.info(" Initialized new Git repo.")
    else:
        repo = Repo(REPO_DIR)
        logging.info(" Loaded existing Git repo.")

    # Change into repo directory
    os.chdir(REPO_DIR)

    # Create and checkout branch
    if BRANCH_NAME not in repo.heads:
        repo.create_head(BRANCH_NAME)
    repo.head.reference = repo.heads[BRANCH_NAME]
    repo.head.reset(index=True, working_tree=True)
    logging.info(f" Switched to branch: {BRANCH_NAME}")

    # Create dummy file
    dummy_file = "dummy_feature.txt"
    with open(dummy_file, "w") as f:
        f.write("This is a test file created on a feature branch using GitPython.\n")
    logging.info(f" Created file: {dummy_file}")

    #  Copy this script into repo (only once)
    script_name = "git_python_test.py"
    script_source = os.path.join("..", script_name)
    if os.path.exists(script_source):
        shutil.copy(script_source, script_name)
        logging.info(f" Copied {script_name} into the Git repo.")

    # Stage and commit both files
    repo.index.add([dummy_file, script_name])
    repo.index.commit("Add dummy file and git_python_test.py to repo")
    logging.info(" Committed script and data file.")

    # Print commits
    logging.info(" Commit History:")
    for commit in repo.iter_commits():
        logging.info(f"{commit.hexsha[:7]} - {commit.author.name}: {commit.message.strip()}")

    # Add remote if not added
    if "origin" not in [remote.name for remote in repo.remotes]:
        repo.create_remote("origin", url=GITHUB_REPO_URL)
        logging.info(" Added GitHub remote.")

    # Push
    repo.remote("origin").push(refspec=f"{BRANCH_NAME}:{BRANCH_NAME}")
    logging.info(" Pushed branch and script to GitHub.")

except GitCommandError as git_err:
    logging.error(f" Git error: {git_err}")
except Exception as e:
    logging.error(f" Unexpected error: {e}")
