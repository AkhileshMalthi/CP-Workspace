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
# Solution
#------------------------------------------------------------------------------
def solution() -> Union[List[int], int, str]:
    # write code
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
            print(*result)
        else:
            print(result)

if __name__ == "__main__":
    main()
