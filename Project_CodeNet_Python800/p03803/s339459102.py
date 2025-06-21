#k = int(input())
#s = input()
#a, b = map(int, input().split())
#s, t = map(str, input().split())
#l = list(map(int, input().split()))
#l = [list(map(int,input().split())) for i in range(n)]

a, b = map(int, input().split())

if (a == 1):
    a = 14
if (b == 1):
    b = 14

if (a > b):
    print("Alice")
elif (a < b):
    print("Bob")
else:
    print("Draw")

