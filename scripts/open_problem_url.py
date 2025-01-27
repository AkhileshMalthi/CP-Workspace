import json
import webbrowser
from run_testcases import get_latest_cph_file

def open_problem_url():
    try:
        # Get latest test file
        test_file = get_latest_cph_file()
        
        # Load problem data from .prob file
        with open(test_file, 'r', encoding='utf-8') as f:
            prob_data = json.load(f)
            url = prob_data.get('url')
            
            if not url:
                raise Exception("No URL found in problem file")
            
            print(f"Opening URL: {url}")
            webbrowser.open(url)
            
    except Exception as e:
        print(f"Error opening URL: {e}")

if __name__ == "__main__":
    open_problem_url()
