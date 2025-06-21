number, base = map(int, input().split())
result_list = []
while number / base > 0:
  mod = number % base
  result_list.append(str(mod))
  number = number // base

result_list.reverse()
result = "".join(result_list)
print(len(result))
