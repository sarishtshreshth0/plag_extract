from collections import defaultdict
import heapq
def solve():
    N,M = map(int,input().split())
    day_fee = defaultdict(list)
    for i in range(N):
        a, b = map(int,input().split())
        day_fee[a].append(b)

    fee_heap = []
    heapq.heapify(fee_heap)

    ans = 0
    for day in range(1,M+1):
        for fee in day_fee[day]:
            heapq.heappush(fee_heap, -fee)
        
        if len(fee_heap) != 0:
            ans += -heapq.heappop(fee_heap)
    
    print(ans)

if __name__ == '__main__':
    solve()