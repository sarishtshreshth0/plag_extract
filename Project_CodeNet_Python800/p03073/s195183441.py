S=input()

st1 = 0
st0 = 0

for i in range(len(S)):
    if S[i] == '1' and i%2==0:
        st0+=1
    elif S[i] == '0' and i%2==0:
        st1+=1
    elif S[i] == '1' and i%2!=0:
        st1+=1
    elif S[i] == '0' and i%2!=0:
        st0+=1

print(min(st1, st0))