def main():
    import sys
    from heapq import heappop, heappush
    from collections import deque

    def input(): return sys.stdin.readline().rstrip()

    def check(k):
        tmp = str(k)
        flag = 1
        if len(tmp) > 2:
            for s in nums:
                flag &= (s in tmp)
            if flag: 
                return True
        return False

    n = int(input())
    num = [3, 5, 7]
    nums = ['3', '5', '7']
    que = deque([3, 5, 7])
    cnt = 0
    while que:
        x = que.popleft()
        if x > n:
            break
        if check(x):
            cnt += 1
        for i in num:
            que.append(10*x+i)
    print(cnt)


    
if __name__ == '__main__':
    main()