from collections import deque

N = int(input())
result = set()

queue = deque([3, 5, 7])

count = 0
while queue:
    number = queue.pop()

    if number <= N:
        string = str(number)
        if '3' in string and '5' in string and '7' in string:
            result.add(number)
        for i in range(3, 8, 2):
            queue.appendleft(number * 10 + i)

print(len(result))
