# import math
# import statistics
# a=input()
#b,c=int(input()),int(input())
# c=[]
# for i in a:
#     c.append(i)
e1,e2,e3 = map(int,input().split())
#f = list(map(int,input().split()))
#g = [input() for _ in range(a)]
# h = []
# for i in range(e1):
#     h.append(list(map(int,input().split())))

if e1<=e3<=e2 or e2<=e3<=e1:
    print("Yes")
else:
    print("No")