import os
import shutil
import sys

DIR = "code_submissions"

def move_solution():
    try:
        # Get source file - use active file if provided
        source_file = os.getenv('VSCODE_ACTIVE_FILE')
        if not source_file or not os.path.exists(source_file):
            print(f"Error: No valid source file found")
            return
            
        # Get default problem name from filename without extension
        default_name = os.path.splitext(os.path.basename(source_file))[0]
        
        # Ask user for problem name, use default if empty
        user_input = input(f"Enter problem name (press Enter to use '{default_name}'): ").strip()
        problem_name = user_input if user_input else default_name
            
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
