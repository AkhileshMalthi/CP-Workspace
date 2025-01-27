import json
from run_testcases import get_latest_cph_file

def get_first_testcase():
    try:
        # Get latest test file
        test_file = get_latest_cph_file()
        
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
