import sys
import time
from main import solution

sys.stdin = open("io_files/input.txt", "r")
sys.stdout = open("io_files/output.txt", "a")

start_time = time.time()
solution()
end_time = time.time()

execution_time = end_time - start_time
# print("\n"+ "-"*50 + f"\nExecution time: {execution_time:.6f} seconds")
print("\n"+ "-"*50 + f"\nExecution time: {execution_time*1000:.6f} ms")

