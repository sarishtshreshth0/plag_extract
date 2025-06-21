import sys

readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
read = sys.stdin.buffer.read
sys.setrecursionlimit(10 ** 7)
INF = float('inf')

N = int(input())

def F(list_):
    if list_ and int("".join(map(str, list_))) > N:
        return
    
    if 3 in list_ and 5 in list_ and 7 in list_:
        yield 1
    
    for v in [3, 5, 7]:
        list_.append(v)
        yield from F(list_)
        list_.pop()
    return

ans = sum(F([]))
print(ans)