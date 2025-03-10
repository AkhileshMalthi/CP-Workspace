import json
import os
from run_testcases import get_latest_cph_file

def get_current_file():
    solution_file = os.getenv('SOLUTION_FILE', 'main.py')
    return os.path.basename(solution_file)

def get_first_testcase():
    try:
        # Get current file name
        current_file = get_current_file()
        
        # Get latest test file matching the current solution
        test_file = get_latest_cph_file(current_file)
        
        # Load test cases from .prob file
        with open(test_file, 'r', encoding='utf-8') as f:
            prob_data = json.load(f)
            tests = prob_data.get('tests', [])
            
            if not tests:
                raise Exception("No tests found in problem file")
            
            # Get first test case input
            first_test = tests[0].get('input', '').strip()
            
            # Write to input.txt
            with open('io_files/input.txt', 'w') as f:
                f.write(first_test)
            
            print(f"First test case written to input.txt:\n{first_test}")
            
    except Exception as e:
        print(f"Error getting first test case: {e}")

if __name__ == "__main__":
    get_first_testcase()
