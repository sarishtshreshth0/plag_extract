A,B = list(map(int,input().split()))
out = "No"
for i in range(1,4):
    if A*B*i%2==1:
        out = "Yes"

print(out)
