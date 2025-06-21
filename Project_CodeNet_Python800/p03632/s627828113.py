time_list = [ int(i) for i in input().split()]

a = time_list[0]
b = time_list[1]
c = time_list[2]
d = time_list[3]

output = 0
if b < c or d < a:
    output = 0
else:
    output = min(b,d) - max(a,c)

print(output)