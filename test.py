import os
import subprocess
import random
from datetime import datetime, timedelta

# Configuration
REPO_PATH = "/Users/paulodrefahl/Desktop/Projects /DS-ALG/data-structures-algorithms-practice"  # Replace with your GitHub repo path
BRANCH_NAME = "main"  # Replace with your branch name if different
START_DATE = "2024-01-24"  # Starting date in YYYY-MM-DD format
END_DATE = "2024-12-31"  # Ending date in YYYY-MM-DD format
COMMIT_PREFIX = "DS"  # Prefix for commit messages

def run_command(command, cwd=None):
    """Run a shell command and capture the output."""
    result = subprocess.run(command, cwd=cwd, text=True, capture_output=True)
    if result.returncode != 0:
        print(f"Error: {result.stderr.strip()}")
        exit(1)
    return result.stdout.strip()

def commit_with_date(repo_path, commit_message, commit_date, branch_name):
    """Add, commit, and push changes to GitHub with a specific commit date."""
    os.chdir(repo_path)
    print(f"Adding changes for commit dated {commit_date}...")
    run_command(["git", "add", "."])
    run_command([
        "git", "-c", f"user.date={commit_date}", "commit", "--date", commit_date, "-m", commit_message
    ])
    print(f"Pushing commit dated {commit_date}...")
    run_command(["git", "push", "origin", branch_name])
    print(f"Commit for {commit_date} pushed successfully!")

def main():
    if not os.path.exists(REPO_PATH):
        print(f"Error: Repository path '{REPO_PATH}' does not exist.")
        return

    # Initialize start and end dates
    current_date = datetime.strptime(START_DATE, "%Y-%m-%d")
    end_date = datetime.strptime(END_DATE, "%Y-%m-%d")
    commit_counter = 1

    while current_date <= end_date:
        # Generate commit message
        commit_message = f"{COMMIT_PREFIX} {commit_counter}.v"
        
        # Format date for the commit
        commit_date = current_date.strftime("%Y-%m-%dT%H:%M:%S")
        
        # Perform the commit
        commit_with_date(REPO_PATH, commit_message, commit_date, BRANCH_NAME)
        
        # Increment commit counter
        commit_counter += 1
        
        # Randomly choose the number of days to add (2, 3, or 4 days)
        days_to_add = random.choice([2, 3, 4])
        current_date += timedelta(days=days_to_add)

if __name__ == "__main__":
    main()
