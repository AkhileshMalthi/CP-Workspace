import os
import shutil
import sys

DIR = "code_submissions"

def move_solution():
    try:
        # Get source file - use active file if provided, otherwise default to main.py
        source_file = os.getenv('VSCODE_ACTIVE_FILE', 'main.py')
        if not os.path.exists(source_file):
            print(f"Error: Source file {source_file} not found")
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
        shutil.move(source_file, dest_path)
        print(f"File moved to: {dest_path}")
        
    except Exception as e:
        print(f"Error moving file: {e}")

if __name__ == "__main__":
    move_solution()
