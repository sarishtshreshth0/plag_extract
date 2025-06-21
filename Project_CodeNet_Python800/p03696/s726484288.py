def main():
    from collections import deque

    N = int(input())
    s = input()

    ans = deque(s)
    cnt = 0
    for c in s:
        if c == ')':
            if cnt:
                cnt -= 1
            else:
                ans.appendleft('(')
        else:
            cnt += 1

    for _ in range(cnt):
        ans.append(')')

    print(''.join(ans))


if __name__ == '__main__':
    main()

# import sys
# input = sys.stdin.readline
# 
# sys.setrecursionlimit(10 ** 7)
# 
# (int(x)-1 for x in input().split())
# rstrip()
#
# def binary_search(*, ok, ng, func):
#     while abs(ok - ng) > 1:
#         mid = (ok + ng) // 2
#         if func(mid):
#             ok = mid
#         else:
#             ng = mid
#     return ok
