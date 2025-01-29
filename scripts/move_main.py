import os
import shutil
import sys

DIR = "code_submissions"

def save_problem():
    try:
        problem_name = input("Enter problem name: ").strip()
        if not problem_name:
            print("Error: Problem name cannot be empty")
            return
            
        # Ensure DIR directory exists
        os.makedirs(DIR, exist_ok=True)
        
        # Create destination path
        dest_path = os.path.join(DIR, f"{problem_name}.py")
        
        # Copy the file
        shutil.copy2("main.py", dest_path)
        print(f"Problem saved as: {dest_path}")
        
    except Exception as e:
        print(f"Error saving problem: {e}")

if __name__ == "__main__":
    save_problem()
