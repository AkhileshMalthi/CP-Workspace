from collections import defaultdict, deque, Counter
from heapq import heapify, heappop, heappush, heappushpop
from bisect import bisect_left, bisect_right
from io import IOBase
from itertools import accumulate, permutations, combinations
import math
import sys

sys.setrecursionlimit(10**9)
MOD = 10**9 + 7
INF = float('inf')

"""Input & Output"""
input = sys.stdin.readline
output = sys.stdout.write


int_inp = lambda: int(input())
str_inp = lambda: input().strip()
list_inp = lambda: list(map(int, input().split()))
map_inp = lambda: map(int, input().split())


"""Fast I/O"""
BUFSIZE = 8192


class FastIO(IOBase):
    newlines = 0

    def __init__(self, file):
        self._fd = file
        self.buffer = bytearray(BUFSIZE)
        self.buffer_pointer = 0
        self.bufflen = 0

    def flush(self):
        if self.bufflen > 0:
            self._fd.write(self.buffer[:self.bufflen])
            self.bufflen = 0

    def fill_buffer(self):
        s = self._fd.read(BUFSIZE)
        if s:
            self.buffer[0:len(s)] = s
            self.bufflen = len(s)
            self.buffer_pointer = 0
        else:
            self.bufflen = -1

    def readline(self):
        while self.bufflen == 0 or self.buffer_pointer >= self.bufflen:
            self.fill_buffer()
            if self.bufflen == -1:
                return ""
        line_start = self.buffer_pointer
        while self.bufflen != 0 and self.buffer[self.buffer_pointer] != ord("\n"):
            self.buffer_pointer += 1
        if self.buffer_pointer > line_start:
            r = self.buffer[line_start:self.buffer_pointer].decode()
            self.buffer_pointer += 1
            return r
        else:
            return ""

    def read(self, n):
        if n > self.bufflen - self.buffer_pointer:
            r = self.buffer[self.buffer_pointer:]
            self.fill_buffer()
            if self.bufflen == -1:
                return r
            return r + self.read(n - len(r))
        else:
            r = self.buffer[self.buffer_pointer:self.buffer_pointer + n]
            self.buffer_pointer += n
            return r


sys.stdin = FastIO(sys.stdin)
sys.stdout = FastIO(sys.stdout)


"""Functions"""


def solve():
    # Write your solution here
    pass


if __name__ == "__main__":
    for _ in range(int_inp()):
        solve()