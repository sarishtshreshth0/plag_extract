s = list(map(int, input()))

a = [i%2 for i in range(len(s))]
b = [(i+1)%2 for i in range(len(s))]

a_sum = sum(abs(x-y) for x, y in zip(s, a))
b_sum = sum(abs(x-y) for x, y in zip(s, b))
print(min(a_sum, b_sum))
