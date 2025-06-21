S = input()
n = len(S)
counter2n0=0
counter2n1=0
counter1n0=0
counter1n1=0
for i in range(n):
    if i%2 ==0:
        if S[i] == '0':
            counter2n0 +=1
        else:
            counter2n1 +=1
    if i%2 == 1:
        if S[i] == '0':
            counter1n0 +=1
        else:
            counter1n1 +=1
print(min(counter2n0+counter1n1,counter2n1+counter1n0))
