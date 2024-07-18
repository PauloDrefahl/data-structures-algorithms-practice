import os
import subprocess

# Configuration 2

REPO_PATH = "/Users/paulodrefahl/Desktop/Projects/DS-ALG/data-structures-algorithms-practice"  # Replace with the path to your GitHub repository
COMMIT_MESSAGE = "DS 2.3v"  # Set your commit message
COMMIT_DATE = "2024-07-18T08:00:00"  # Format: YYYY-MM-DDTHH:MM:SS
BRANCH_NAME = "main"  # Replace with your branch name if different

def run_command(command, cwd=None):
    """Run a shell command and capture the output."""
    result = subprocess.run(command, cwd=cwd, text=True, capture_output=True)
    if result.returncode != 0:
        print(f"Error: {result.stderr.strip()}")
        exit(1)
    return result.stdout.strip()

def main():
    # Change to the repository directory
    if not os.path.exists(REPO_PATH):
        print(f"Error: Repository path '{REPO_PATH}' does not exist.")
        return
    os.chdir(REPO_PATH)
    
    # Add changes
    print("Adding changes...")
    run_command(["git", "add", "."])
    
    # Commit changes with a custom date
    print("Committing changes...")
    run_command([
        "git", "-c", f"user.date={COMMIT_DATE}", "commit", "--date", COMMIT_DATE, "-m", COMMIT_MESSAGE
    ])
    
    # Push to GitHub
    print("Pushing changes to GitHub...")
    run_command(["git", "push", "origin", BRANCH_NAME])
    
    print("Changes successfully committed and pushed to GitHub.")

if __name__ == "__main__":
    main()
