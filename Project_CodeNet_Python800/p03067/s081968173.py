from sys import stdin

a,b,c = [int(x) for x in stdin.readline().rstrip().split()]

if a < c < b or b < c < a:
    print("Yes")
else:
    print("No")