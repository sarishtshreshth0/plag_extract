#!/usr/bin/python3
# -*- coding:utf-8 -*-

from collections import defaultdict

def main():
  n = int(input())
  la = list(map(int, input().split()))
  cs_la = [0] * n
  for i in range(n):
    cs_la[i] += (cs_la[i-1] + la[i])
  
  cnts = defaultdict(int)
  for i in range(n):
    cnts[cs_la[i]] += 1
    
  cnt = 0
  for k, v in cnts.items():
    if k == 0:
      cnt += v
    cnt += ( v * (v-1) ) // 2
  print(cnt)
  
if __name__=='__main__':
  main()

