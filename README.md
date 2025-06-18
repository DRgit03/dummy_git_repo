
```markdown
# GitPython Dummy Automation

This repository demonstrates how to automate basic Git operations using Python and the [`GitPython`](https://gitpython.readthedocs.io/en/stable/) library.

The goal is to simulate local Git interactions — such as repository initialization, file creation, committing, branching, and pushing to GitHub — all through a Python script. This is particularly useful for scripting workflows in CI/CD, DevOps, and data automation tasks.

---

##  Project Structure

```

Git-Python\_Dummy\_Script/
├── .env                      # Contains GITHUB\_TOKEN (secure, not committed)
├── .gitignore                # Excludes .env and other sensitive files
├── README.md                 # This file (should be copied into dummy\_git\_repo/)
├── git\_python\_test.py        # Python script that automates Git operations
└── dummy\_git\_repo/           # Actual Git repository folder
├── .git/                 # Git tracking data
├── dummy.txt             # Pre-existing or second commit file
├── dummy\_feature.txt     # Dummy file created by the script
└── git\_python\_test.py    # Script copied and committed into the repo

````

---

##  Features

- Initializes a Git repository (if not already initialized)
- Creates a new branch called `feature-branch`
- Adds a dummy file (`dummy_feature.txt`)
- Copies and commits its own script (`git_python_test.py`)
- Pushes everything to GitHub using a Personal Access Token

---

##  Prerequisites

- Python 3.8 or above
- Git installed and available in your system PATH
- GitHub Personal Access Token (with `repo` scope)

---

##  Installation

### 1. Install required packages:
```bash
pip install gitpython python-dotenv
````

### 2. Create a `.env` file:

This stores your GitHub token securely.

```env
GITHUB_TOKEN=ghp_your_real_token_here
```

### 3. (Optional) Store GitHub credentials:

To cache your credentials after one-time login:

```bash
git config --global credential.helper store
```

Then run a manual `git push` once to store your token-based login.

---
##  How to Run

From the parent folder (`Git-Python_Dummy_Script/`), run:

```bash
python git_python_test.py
```

The script will:

* Copy itself into the repo folder
* Commit both the script and dummy file
* Push to the `feature-branch` on GitHub

---

##  Expected Output

Example logs:

```
 Initialized new Git repo.
 Created dummy_feature.txt
 Copied git_python_test.py into Git repo
 Committed all files
 Pushed feature-branch to GitHub
```

---

##  Best Practices Followed

*  `.env` used for secure credential storage
*  `.gitignore` prevents accidental commits of secrets
*  Branching model used (`feature-branch`)
*  Token-based GitHub authentication

---

## Author

Developed by **Ramu Munnangi**
Project: Git Automation using Python for workflow validation and DevOps scripting experiments.

---

## License

This repository is intended for educational and automation scripting purposes. Feel free to fork and build upon it!

```
