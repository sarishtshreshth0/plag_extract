X=int(input())
cnt_500 = int(X/500)
cnt_5 = int((X%500)/5)
print(1000*cnt_500+cnt_5*5)
