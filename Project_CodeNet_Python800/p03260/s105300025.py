linha = input()
A,B = [int(n) for n in linha.split()]
achou = 0
for x in range(1,4):
    resultado = A * B * x
    if resultado % 2 == 1:
        print("Yes")
        achou = 1
        break
if achou == 0:
    print("No")