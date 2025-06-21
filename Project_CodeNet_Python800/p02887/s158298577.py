#!/usr/bin/env python3
n,s = open(0).read().split()
print(1+sum(s[i-1]!=s[i] for i in range(1,int(n))))
