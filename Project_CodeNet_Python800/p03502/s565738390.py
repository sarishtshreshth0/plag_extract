#k = int(input())
#s = input()
#a, b = map(int, input().split())
#s, t = map(str, input().split())
#l = list(map(int, input().split()))
#l = [list(map(int,input().split())) for i in range(n)]
#a = [list(input()) for _ in range(n)]
#a = [int(input()) for _ in range(n)]

n = input()

f = 0
for i in range(len(n)):
    f += int(n[i])

if (int(n) % f == 0):
    print("Yes")
else:
    print("No")


