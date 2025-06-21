#A - Ice Tea Store
Q,H,S,D = map(int,input().split())
N = int(input())

Q1,H1 = 4*Q,2*H
S = min(Q1,H1,S)

if 2*S>D:
    cnt_2 = N//2
    cnt_1 = N%2
    pay = D*cnt_2 + S*cnt_1
else:
    pay = N * S
print(pay)