#!/usr/bin/env python3

#------------------------------------------------------------------------------
# Imports
#------------------------------------------------------------------------------
# Standard library imports
import sys
import os
# import math

# # Data structure imports
# import heapq
# from collections import (
#     defaultdict,
#     Counter,
#     deque
# )

# Type hints
from typing import (
    List, Set, Dict, Tuple,
    Optional, Union, Any
)

# # Itertools
# from itertools import (
#     permutations,
#     combinations
# )

#------------------------------------------------------------------------------
# Constants
#------------------------------------------------------------------------------
# inf = float('inf')
# mod = 1000000007


#------------------------------------------------------------------------------
# Debug Helper
#------------------------------------------------------------------------------
DEBUG = os.getenv("DEBUG", "0") == "1"

def debug(*args, **kwargs):
    if DEBUG:
        with open("io_files/debug.txt", 'w') as debug_file:
            print(*args, file=debug_file, **kwargs)


#------------------------------------------------------------------------------
# Solution
#------------------------------------------------------------------------------
def solution() -> Union[List[int], int, str]:
    # Write your solution here
    return "Answer"
    
#------------------------------------------------------------------------------
# Main
#------------------------------------------------------------------------------
def main() -> None:
    t = 1
    # t = int(input())
    for _ in range(t):
        result = solution()
        if isinstance(result, (list, tuple, set)):
            sys.stdout.write(' '.join(map(str, result)) + '\n')
        else:
            sys.stdout.write(str(result) + '\n')
        sys.stdout.flush()

if __name__ == "__main__":
    # Local mode 
    if DEBUG:
        sys.stdin = open("io_files/input.txt", "r")
        sys.stdout = open("io_files/output.txt", "w")
    
    main()
