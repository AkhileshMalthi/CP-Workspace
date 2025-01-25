import os
import shutil
import sys

DIR = "code_submissions"

def move_active_file():
    try:
        # Get active file path from environment variable
        active_file = os.getenv('VSCODE_ACTIVE_FILE')
        if not active_file:
            print("Error: No active file found")
            return
            
        problem_name = input("Enter problem name: ").strip()
        if not problem_name:
            print("Error: Problem name cannot be empty")
            return
            
        # Ensure DIR directory exists
        os.makedirs(DIR, exist_ok=True)
        
        # Create destination path
        dest_path = os.path.join(DIR, f"{problem_name}.py")
        
        # Move the file
        shutil.move(active_file, dest_path)
        print(f"File moved to: {dest_path}")
        
    except Exception as e:
        print(f"Error moving file: {e}")

if __name__ == "__main__":
    move_active_file()
