import json
import os
import glob
from importlib.util import spec_from_file_location, module_from_spec
from collections.abc import Iterable

def format_output(output):
    if output is None:
        return ""
    if isinstance(output, (str, int, float)):
        return str(output).strip()
    if isinstance(output, Iterable):
        # Convert each item to string and join with spaces
        return " ".join(str(item).strip() for item in output).strip()
    return str(output).strip()

def get_current_file():
    solution_file = os.getenv('SOLUTION_FILE', 'main.py')
    return os.path.basename(solution_file)

def get_latest_cph_file(current_file=None):
    # Get all .prob files in .cph directory
    cph_files = glob.glob(".cph/*.prob") + glob.glob(".cph/.*.prob")
    if not cph_files:
        print("Searching in:", os.path.abspath(".cph"))
        print("Current working directory:", os.getcwd())
        raise Exception("No test files found in .cph directory")
    
    # First try to find a matching file for current solution
    if current_file:
        base_name = os.path.splitext(current_file)[0]
        for prob_file in cph_files:
            if base_name in prob_file:
                print(f"Found matching test file: {prob_file}")
                return prob_file
    
    # Fall back to latest file if no match found
    latest_file = max(cph_files, key=os.path.getmtime)
    print(f"No matching file found, using latest test file: {latest_file}")
    return latest_file

def load_solution():
    # Get solution file path from environment variable or default to main.py
    solution_file = os.getenv('SOLUTION_FILE', 'main.py')
    
    # Import the solution function from the specified file
    module_name = os.path.splitext(os.path.basename(solution_file))[0]
    spec = spec_from_file_location(module_name, solution_file)
    module = module_from_spec(spec)
    spec.loader.exec_module(module)
    return getattr(module, "solution", None)

def run_test_cases():
    try:
        # Get current file name and find matching test file
        current_file = get_current_file()
        test_file = get_latest_cph_file(current_file)
        
        # Load test cases from .prob file
        with open(test_file, 'r', encoding='utf-8') as f:
            prob_data = json.load(f)
            tests = prob_data.get('tests', [])
            if not tests:
                raise Exception("No tests found in problem file")
        
        # Get the solution function
        solution_func = load_solution()
        if not solution_func:
            raise Exception("No 'solution' function found in main.py")
        
        # Initialize passed counter
        passed = 0
        total = len(tests)
        
        print(f"\nRunning {total} tests from {os.path.basename(test_file)}:")
        print("-" * 40)
        
        passed_cases = []
        failed_cases = []
        
        for i, test in enumerate(tests, 1):
            input_data = test.get('input', '')
            expected = format_output(test.get('output', ''))
            
            print(f"\nTest Case #{i}:")
            print(f"Input:")
            print(f"{input_data.strip()}")
            
            # Run solution
            import io
            import sys
            original_stdin = sys.stdin
            sys.stdin = io.StringIO(input_data)
            
            try:
                solution_output = solution_func()
                result = format_output(solution_output)
                print(f"Your Output:")
                print(f"{result}")
                print(f"Expected Output:")
                print(f"{expected}")
                
                if result == expected:
                    passed_cases.append(i)
                    print("\033[32m" + f"✓ Test #{i} PASSED" + "\033[0m")
                    passed += 1
                else:
                    failed_cases.append(i)
                    print("\033[31m" + f"✗ Test #{i} FAILED" + "\033[0m")
            except Exception as e:
                failed_cases.append(i)
                print("\033[31m" + f"✗ Test #{i} ERROR: {str(e)}" + "\033[0m")
            finally:
                sys.stdin = original_stdin
            
            print("-" * 40)
        
        # Print summary
        print(f"\nSummary: {passed}/{total} tests passed")
        if passed_cases:
            print("\033[32m" + f"Passed Cases: {passed_cases}" + "\033[0m")
        if failed_cases:
            print("\033[31m" + f"Failed Cases: {failed_cases}" + "\033[0m")
        
    except Exception as e:
        print(f"Error running tests: {e}")

if __name__ == "__main__":
    run_test_cases()
