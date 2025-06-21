A,B,C = map(int, input().split())
print("YNeos"[(B-C)*(C-A)<0::2])