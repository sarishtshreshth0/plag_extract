import sys
input = sys.stdin.readline

input_array = []
input_array.append(input().split())

for i in input_array:
    print(int(int(i[0]) + int(i[1])/2))
