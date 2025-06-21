from collections import deque
def bfs(n):
    ans = 0
    queue = deque([3,5,7])

    while queue:
        num = queue.popleft()

        if num > n:
            return ans

        for i in [3,5,7]:
            queue.append(num*10+i)

        st = str(num)
        if '3' in st and '5' in st and '7' in st:
            ans += 1


n = int(input())
print(bfs(n))