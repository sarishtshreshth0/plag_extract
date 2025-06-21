inputs = list(map(int, input().split(" ")))
print('Yes' if (inputs[0] < inputs[2] < inputs[1] or inputs[1] < inputs[2] < inputs[0]) else 'No')