#!/usr/bin python3
# -*- coding: utf-8 -*-

# 優先度付きキュー
# 優先度とフラグを入れ込んだキューで、優先度が大きいものからポップできる
# 優先度が小さいものとする場合は、マイナスでキューにプッシュする
# hp キュー
# hist フラグの履歴（一度読んだものは再度使わない場合）

from heapq import heapify, heappop, heappush, heappushpop

def main():
    N, M = map(int, input().split())
    S = {}
    for i in range(N):
        a,b = map(int,(input().split()))
        if a in S.keys():
            S[a].append((-b,a))
        else:
            S[a]=[(-b,a)]
    hp = []
    heapify(hp)
    ret = 0
    for i in range(1,M+1):
        if i in S:
            for jb in S[i]:
                heappush(hp, jb)
        if len(hp)==0:
            continue
        x = heappop(hp)
        ret += -x[0]
    print(ret)

if __name__ == '__main__':
    main()