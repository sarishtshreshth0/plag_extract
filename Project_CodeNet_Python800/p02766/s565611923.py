# coding: utf-8
# Your code here!

n,k=map(int,input().split())
a=[]
while n>=1:
    s=n%k
    n=n//k
    a.append(s)

print(len(a))