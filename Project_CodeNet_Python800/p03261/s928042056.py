N = int(input())
Word = [input()]
Flag = True
for T in range(0,N-1):
    New = input()
    if Word[-1][-1]==New[0] and New not in Word:
        Word.append(New)
    else:
        Flag = False
        break
if Flag: print('Yes')
else: print('No')