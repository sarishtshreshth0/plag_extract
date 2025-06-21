S=input()
n=len(S)
print(min(sum(x!=y for x,y in zip(S,('01'*(n//2+1))[:n])),sum(x!=y for x,y in zip(S,('10'*(n//2+1))[:n]))))