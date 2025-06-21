line = input()
num = [int(n) for n in line.split()][0]
smaller_divisible_number = num
if num%2 != 0:
    smaller_divisible_number *= 2
print(smaller_divisible_number)