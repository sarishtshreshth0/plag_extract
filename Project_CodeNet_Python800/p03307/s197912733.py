"""
author : halo2halo
date : 24, Jan, 2020
"""

import sys

# import numpy as np

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

N = int(readline())
print(2 * N if N % 2 == 1 else N)
