import itertools
import functools
import math
from collections import Counter
from itertools import combinations
import re


N,K=map(int,input().split())

cnt = 1
while True:
    if cnt > 10000:
        break

    if N // K**cnt == 0:
        print(cnt)
        exit()
    cnt += 1
