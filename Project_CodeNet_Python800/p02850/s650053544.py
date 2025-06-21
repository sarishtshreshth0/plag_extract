from collections import Counter, defaultdict
import sys
sys.setrecursionlimit(10 ** 5 + 10)
# input = sys.stdin.readline
from math import factorial
import heapq, bisect
import math
import itertools
import queue
from collections import deque
from fractions import Fraction



def main():
    num = int(input())
    data = [list(map(int, input().split())) for i in range(num - 1)]

    node_data = defaultdict(set)
    for i in range(num - 1):
        a, b = data[i]
        node_data[a].add(b)
        node_data[b].add(a)

    ans_num = 0
    for i in range(1, num + 1):
        ans_num = max(ans_num, len(node_data[i]))

    edge_data = defaultdict(int)
    ans_count = 0

    for i in range(1, num + 1):
        now_list = list(node_data[i])
        now_list.sort()
        count = bisect.bisect_left(now_list, i) + 1

        use_set = set()
        for ele in now_list[:count - 1]:
            use_set.add(edge_data[(i, ele)])
        now_indx = 1

        for ele in now_list[count - 1:]:
            while now_indx in use_set:
                now_indx += 1

            edge_data[(i, ele)] = now_indx
            edge_data[(ele, i)] = now_indx
            use_set.add(now_indx)

        ans_count = max(ans_count, now_indx)

    print(ans_count)
    for i in range(num - 1):
        a, b = data[i]
        ans = edge_data[(a, b)]
        print(ans)








if __name__ == '__main__':
    main()

