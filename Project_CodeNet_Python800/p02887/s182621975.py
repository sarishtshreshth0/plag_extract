input()
S = input()
j = ""
A =""
for i in S:
    if i !=j:
        A += i
        j = i
print(len(A))