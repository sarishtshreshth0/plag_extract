N=int(input())
correct = True
words = set({})

W = input()
words.add(W)
last_letter = W[len(W)-1]

for i in range(1,N):
    W = input()
    if  not W in words and W[0] == last_letter:
        words.add(W)
        last_letter = W[len(W)-1]
    else:
        correct = False
        break

if correct:
    print('Yes')
else:
    print('No')
