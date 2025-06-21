import sys
input = sys.stdin.readline
import heapq

def main():
    """
    q:0.25l
    h:0.5l
    s:1l
    d:2l
    """
    q, h, s, d = [int(i) for i in input().strip().split()]
    n = int(input().strip())
    
    prices = list()
    heapq.heappush(prices, (q * 4, q, 0.25))
    heapq.heappush(prices, (h * 2, h, 0.5))
    heapq.heappush(prices, (s, s, 1))
    heapq.heappush(prices, (d / 2, d, 2))

    ans = 0
    _,price,size = heapq.heappop(prices)
    
    while n != 0:
        if size > n:
            _, price, size = heapq.heappop(prices)
            continue
        else:
            if size >= 1:
                ammount = n // size
                n = n % size
                ans += price * ammount
                continue
            else:
                ammount = int(n / size)
                ans += price * ammount
                break
    print(ans)
    return



if __name__ == "__main__":
    main()