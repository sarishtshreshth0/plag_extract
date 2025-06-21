from sys import stdin

x,y = [int(x) for x in stdin.readline().rstrip().split()]

print(x+y//2)