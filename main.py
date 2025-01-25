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
    """Print debug messages when DEBUG mode is enabled"""
    if DEBUG:
        with open("io_files/debug.txt", 'w') as debug_file:
            print(*args, file=debug_file, **kwargs)


#------------------------------------------------------------------------------
# Solution
#------------------------------------------------------------------------------
def solution() -> Union[List[int], int, str]:
    """
    Main solution function
    Returns:
        Union[List[int], int, str]: Solution result
    """ 

    n, d = map(int, input().split())
    friends = [list(map(int, input().split())) for _ in  range(n)]
    friends.sort(key=lambda x: x[0])

    left = right = ans = sum = 0

    while right < n:
        sum += friends[right][1]
        
        while friends[right][0] >= friends[left][0] + d:
            sum -= friends[left][1]
            left += 1
        
        ans = max(ans, sum)
        right += 1

    return ans
    
#------------------------------------------------------------------------------
# Main
#------------------------------------------------------------------------------
def main() -> None:
    """Main function handling I/O"""
    result = solution()
    if isinstance(result, (list, tuple, set)):
        sys.stdout.write(' '.join(map(str, result)) + '\n')
    else:
        sys.stdout.write(str(result) + '\n')
    sys.stdout.flush()

if __name__ == "__main__":
    # Debug mode setup
    if DEBUG:
        sys.stdin = open("io_files/input.txt", "r")
        sys.stdout = open("io_files/output.txt", "w")
    
    """
    # For multiple test cases
    t = get_int()
    for _ in range(t):
        main()
    """
    
    # For single test case
    main()
