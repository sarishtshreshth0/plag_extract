N = int(input())
S = input()
A = ['']
for i in S:
    if i != A[-1]:
        A.append(i)
print(len(''.join(A)))