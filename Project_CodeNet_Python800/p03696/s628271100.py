n=int(input())
s=input()

while True:
    cum=[0]*(len(s)+1)
    for i,c in enumerate(s):
        cum[i+1]=cum[i]-1 if c==')' else cum[i]+1
    min_=min(cum)
    if min_<0:
        s='('*abs(min_)+s
        continue
    r=cum[-1]
    if r>0:
        s=s+')'*r
        continue
    print(s)
    exit()