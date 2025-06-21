#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math
n, k = map(int, input().split())
r=0
while n > 0:
  r=r+1
  n=n//k
print(r)
