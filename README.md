# Git History Cleaner

This Python script is designed to help you completely clean your Git repository's commit history. It creates a new branch with no prior commit history, adds all the current files, and force pushes this new state as the main branch. This can be useful when you want to scrub sensitive data from your history or just want to start fresh without the weight of old commits.

## Prerequisites

- Git must be installed on your system.
- You must be logged in with SSH to use this script without credential prompts.

## Usage

- To use this script, you will need to provide the directory of the Git repository you want to clean and a commit message for the initial commit after cleaning history.

```
python git_history_cleaner.py --directory <path_to_repository> --message "Cleaned"
```

![image](https://github.com/AlbertL7/Git-Commit-History-Cleaner/assets/71300144/546f5b67-07a8-494a-9078-80dbba5ce775)

## Features

- Checks if Git is installed.
- Changes to the specified repository directory.
- Creates a new orphan branch with no commit history.
- Adds all files from the current state of the main branch.
- Commits the current files with a provided commit message.
- Deletes the old main branch and renames the current branch to main.
- Force pushes the new main branch to the remote repository.
- Performs an aggressive garbage collection to prune all unreachable objects.

## Warning

This script will irreversibly change your repository's history. All previous commits will be lost. Use this script with caution and ensure that you have backups of any important data.

## Contributing

Contributions to this script are welcome. Please ensure that your pull requests provide a clear description of the problem and a detailed explanation of the solution.
