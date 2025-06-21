M, D = map(int, input().split())
m = [0] * (M+1)
for i in range(22, D+1):
    if M >= (i//10)*(i%10) > 0 and i%10 >= 2:
        m[(i//10)*(i%10)] += 1
print(sum(m))
