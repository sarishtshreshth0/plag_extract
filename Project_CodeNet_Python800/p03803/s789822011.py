a,b=map(int,input().split())
print(('ADlriacwe'[a==b::2],'Bob')[(a-2)%13<(b-2)%13])