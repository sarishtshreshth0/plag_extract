n = int(input())

l = []
for i in range(1, int(n**.5)+1):
    if n % i == 0:
        a = len(str(i))
        b = len(str(n // i))
        l.append((a,b))

max_list= []
for j in range(len(l)):
    max_list.append(max(l[j][0], l[j][1]))
print(min(max_list))


