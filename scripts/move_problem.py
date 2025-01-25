import os
import shutil
import sys

DIR = "code_submissions"

def move_problem():
    try:
        problem_name = input("Enter problem name: ").strip()
        if not problem_name:
            print("Error: Problem name cannot be empty")
            return
            
        # Ensure DIR directory exists
        os.makedirs(DIR, exist_ok=True)
        
        # Create destination path
        dest_path = os.path.join(DIR, f"{problem_name}.py")
        
        # Move the file
        shutil.move("main.py", dest_path)
        print(f"Problem moved to: {dest_path}")
        
    except Exception as e:
        print(f"Error moving problem: {e}")

if __name__ == "__main__":
    move_problem()
