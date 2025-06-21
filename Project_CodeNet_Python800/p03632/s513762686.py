a,b,c,d = map(int,input().split())
li = [1]*100
for i in range(a):
    li[i] = 0
for i in range(100-b):
    li[i+b] = 0
for i in range(c):
    li[i] = 0
for i in range(100-d):
    li[i+d] = 0
print(li.count(1))