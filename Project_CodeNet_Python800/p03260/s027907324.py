line = input()
num_a, num_b = [int(n) for n in line.split()]
value = "Yes"
if (num_a * num_b)%2 == 0:
    value = "No"
print(value)