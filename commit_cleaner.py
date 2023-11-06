import subprocess
import shutil
import argparse
import os

# Be sure to be logged in with SSH to properly use this script or it will fail when asked for credentials

def is_git_installed():
    """Check if Git is installed."""
    return shutil.which("git") is not None

def run_command(command):
    """Run a command and check if it completed successfully."""
    try:
        print(f"Executing command: {command}", flush=True)
        result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        print(result.stdout, flush=True)
        return True
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while executing: {command}", flush=True)
        print(e.stderr, flush=True)
        return False

def clean_git_history(commit_message, directory):
    if not is_git_installed():
        print("Git is not installed on this system.", flush=True)
        return

    # Change to the specified directory
    if directory:  # Only change directory if one is provided
        try:
            os.chdir(directory)
        except OSError as e:
            print(f"Could not change to directory {directory}: {e}", flush=True)
            return

    # Create a new branch with no commit history
    if not run_command('git checkout --orphan last'):
        return

    # Add all the files from the current state of the main branch
    if not run_command('git add -A'):
        return

    # Commit the current files
    if not run_command(f'git commit -am "{commit_message}"'):
        return

    # Delete the main branch
    if not run_command('git branch -D main'):
        return

    # Rename the current branch to main
    if not run_command('git branch -m main'):
        return

    # Force push the main branch to the remote repository
    if not run_command('git push -f origin main'):
        return

    # Perform an aggressive garbage collection
    print("Starting aggressive garbage collection...", flush=True)
    if not run_command('git gc --aggressive --prune=all'):
        return
    print("Aggressive garbage collection completed.", flush=True)

def main():
    parser = argparse.ArgumentParser(description='Completely clean a GitHub repo\'s commit history.')
    parser.add_argument('-d', '--directory', type=str, help='The directory where the Git repository is located.', required=True)
    parser.add_argument('-m', '--message', type=str, help='Commit message for the initial commit after cleaning history.', required=True)
    args = parser.parse_args()

    clean_git_history(args.message, args.directory)

if __name__ == "__main__":
    main()
