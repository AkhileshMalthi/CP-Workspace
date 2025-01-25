import shutil
import os

def reset_main():
    try:
        template_path = os.path.join('templates', 'main_template.py')
        shutil.copy(template_path, 'main.py')
        print("Successfully reset main.py to template")
    except Exception as e:
        print(f"Error resetting main.py: {e}")

if __name__ == "__main__":
    reset_main()
