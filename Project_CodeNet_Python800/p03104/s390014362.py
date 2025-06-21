A,B=map(int,input().split());B+=1
print(sum(((((B//(2*(2**j)))*(2**j)+max(0,(B%(2*(2**j)))-2**j))-((A//(2*(2**j)))*(2**j)+max(0,(A%(2*(2**j)))-2**j)))%2)*(2**j) for j in range(41)))