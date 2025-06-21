N = int(input())
div,mod = divmod(N,500)
div2 = mod//5
print(1000*div + 5*div2) 