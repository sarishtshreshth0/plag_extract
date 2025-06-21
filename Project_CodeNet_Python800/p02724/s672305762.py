score = int(input())
dama500 = score // 500
dama5 = (score % 500)//5
answer = 1000*dama500+5*dama5
print(answer)