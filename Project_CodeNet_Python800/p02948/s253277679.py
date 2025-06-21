#!/usr/bin/env python3
import sys
import heapq



def main():
    N, M = map(int, input().split())

    # day日目に選択可能になる選択肢をまとめて管理しておく。
    jobs = [[] for _ in range(M + 1)]
    for _ in range(N):
        a, b = map(int, input().split())
        if a > M:
            continue
        jobs[a].append(b)

    heap = []
    salary = 0

    # M日目から遡っていく。
    for day in range(1, M + 1):
        # 選択可能になる選択肢をエンキュー(取り出す時に最大値が欲しいのでマイナスにする。)
        for i in jobs[day]:
            heapq.heappush(heap, -i)
        # ヒープが空でなければ最も良い選択肢を取得、マイナスを戻す。
        if len(heap) > 0:
            salary += abs(heapq.heappop(heap))

    print(salary)
    return

if __name__ == '__main__':
    main()
