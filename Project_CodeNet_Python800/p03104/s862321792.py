A,B=map(int,input().split())
res,B=0,B+1
for j in range(41):
    res+=((((B//(2*(2**j)))*(2**j)+max(0,(B%(2*(2**j)))-2**j))-((A//(2*(2**j)))*(2**j)+max(0,(A%(2*(2**j)))-2**j)))%2)*(2**j)
print(res)