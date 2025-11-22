# CP-Workspace

A streamlined competitive programming workspace for VS Code that integrates with CPH (Competitive Programming Helper) to automate testing and solution management.

## Overview

CP-Workspace is designed for developers practicing Data Structures and Algorithms (DSA) who want a local testing environment with automated workflows. It leverages VS Code's Task system and Python scripts to provide a seamless problem-solving experience.

## Target Audience

This workspace is built for:
- Competitive programmers practicing DSA problems
- Developers using CPH extension as a local judge
- Python programmers who prefer VS Code for competitive programming

## Prerequisites

### Required
- **VS Code**: This workspace is specifically designed for Visual Studio Code
- **Python 3**: All scripts and templates are written in Python 3
- **CPH Extension**: [Competitive Programming Helper](https://marketplace.visualstudio.com/items?itemName=DivyanshuAgrawal.competitive-programming-helper) for fetching test cases from competitive programming platforms

### Optional
- Git for version control

## Installation

1. Clone or download this repository:
   ```bash
   git clone https://github.com/AkhileshMalthi/CP-Workspace.git
   cd CP-Workspace
   ```

2. Install the CPH extension in VS Code:
   - Open VS Code Extensions (Ctrl+Shift+X)
   - Search for "Competitive Programming Helper"
   - Install the extension

3. Open the workspace folder in VS Code

## Project Structure

```
CP-Workspace/
├── .vscode/
│   └── tasks.json          # VS Code task definitions
├── scripts/
│   ├── run_testcases.py    # Run all test cases from CPH
│   ├── get_first_testcase.py # Load first test case to input file
│   ├── move_solution.py    # Move solution to submissions folder
│   ├── move_main.py        # Save main.py solution
│   ├── reset.py            # Reset main.py to template
│   ├── time_solution.py    # Time solution execution
│   └── open_problem_url.py # Open problem URL in browser
├── templates/
│   ├── main_template.py    # Default problem template
│   ├── cph_python_template.py # CPH-specific template
│   └── faster_template.py  # Optimized template
├── io_files/               # Created at runtime
│   ├── input.txt          # Input for local testing
│   ├── output.txt         # Output from solutions
│   ├── debug.txt          # Debug output
│   └── testcases.txt      # Test case storage
├── code_submissions/       # Saved solutions
└── .cph/                   # CPH test case files
```

## Workflow

### 1. Start a New Problem

1. Use CPH extension to fetch a problem from a competitive programming platform
2. CPH will create a `.prob` file in the `.cph` directory with test cases
3. Open `main.py` to start coding your solution

### 2. Write Your Solution

Edit the `solution()` function in `main.py`:

```python
def solution() -> Union[List[int], int, str]:
    # Your solution code here
    n = int(input())
    return n * 2
```

### 3. Test Your Solution

Use VS Code tasks (Ctrl+Shift+P → "Tasks: Run Task"):

- **Run Test Cases**: Execute all test cases from CPH
- **Load First Test Case**: Copy first test case to input.txt
- **Run Problem**: Run with DEBUG mode enabled
- **Time Solution**: Measure execution time

### 4. Save Your Solution

- **Move Solution**: Save the current file to `code_submissions/`
- **Save Main Solution**: Save main.py with a custom name
- **Reset Main File**: Restore main.py to template

### 5. Manage Files

- **Clear Input/Output/Debug/Testcases Files**: Clean individual IO files
- **Clear All IO Files**: Clean all IO files at once

## Available Tasks

Access tasks via `Ctrl+Shift+P` → "Tasks: Run Task":

| Task | Description |
|------|-------------|
| Run Test Cases | Execute all test cases from the .prob file |
| Load First Test Case | Copy the first test case to input.txt |
| Run Problem | Run solution with DEBUG mode |
| Time Solution | Measure solution execution time |
| Reset Main File | Reset main.py to the default template |
| Move Solution | Move current file to code_submissions/ |
| Save Main Solution | Save main.py with a custom name |
| Open Problem URL | Open problem URL in browser |
| Clear Input/Output/Debug Files | Clear individual IO files |
| Clear All IO Files | Clear all IO files at once |
| Done | Move solution, clear files, and close editor |

## Features

- **Automated Testing**: Run all test cases from CPH with colored output
- **Template System**: Quick start with pre-configured templates
- **Debug Mode**: Write debug output to separate file
- **Solution Management**: Organize and archive completed solutions
- **Helper Functions**: Pre-built functions for common DSA operations (prefix sums, sieve, etc.)
- **Type Hints**: Full type hint support for better code clarity

## Limitations

- **VS Code Only**: This workspace requires VS Code and will not work in other editors
- **CPH Dependency**: Currently relies on CPH extension for fetching test cases from platforms
  - Note: An alternative method for test case management is being considered
- **Python Only**: All scripts and templates are Python-based

## Usage Tips

1. **Use DEBUG mode** when developing to write debug output to `io_files/debug.txt`
2. **Leverage templates** in the `templates/` folder for different problem types
3. **Use keyboard shortcuts** to quickly run tasks (configure in VS Code settings)
4. **Save solutions regularly** using the "Move Solution" task to avoid losing work

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests for:
- Bug fixes
- New features
- Template improvements
- Documentation updates

## License

This project is open source and available for anyone to use and modify.
