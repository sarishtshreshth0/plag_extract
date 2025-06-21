import sys
sys.setrecursionlimit(10**7)

def saiki(s):
    global cnt,n
    L = ["3","5","7"]
    if eval(s) <= n:
        if len(set(s)) == 3:
            cnt += 1
        for i in L:
            saiki(s+i)

n = int(input())
cnt = 0
for i in ["3","5","7"]:
    saiki(i)
print(cnt)