import sys,queue,math,copy,itertools,bisect,collections
LI = lambda : [int(x) for x in sys.stdin.readline().split()]

N,M = LI()
data = [LI() for _ in range(N)]
# dp = [0] * (M+1)
# data.sort(key=lambda x:x[1], reverse=True)
#
# N0 = 2 ** M.bit_length()
# seg = [0] * (2*N0)
#
# def seg_set(i,x):
#     i = i + N0- 1
#     seg[i] = x
#     while i > 0:
#         i = (i-1) // 2
#         seg[i] = max(seg[i*2+1],seg[i*2+2])
#
# def seg_query(i):
#     i = i + N0 - 1
#     ret = seg[i]
#     while i ^ (i+1) < i+1:
#         i = (i-2) // 2
#         ret = max(ret,seg[i])
#     return ret
#
# for i in range(M+1):
#     seg_set(i,i)
#
# for a,b in data:
#     if a <= M:
#         i = seg_query(M-a+1)
#         if i > 0:
#             dp[i] = b
#             seg_set(i,0)
# print(sum(dp))
data.sort()
p = 0
q = queue.PriorityQueue()
ans = 0
for i in range(1,M+1):
    while p < N:
        if data[p][0] > i : break
        q.put(-data[p][1])
        p += 1
    if not q.empty():
        ans -= q.get()
print (ans)

