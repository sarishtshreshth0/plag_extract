a,b=[14 if x==1 else x for x in map(int,input().split())]
print("Alice" if a>b else "Draw" if a==b  else "Bob")