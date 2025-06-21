n = int(input())
contador = 0
res = 0
while(True):
    contador += n
    if contador % 2 == 0 and contador % n == 0:
        res = contador
        break;
print(res,'\n')