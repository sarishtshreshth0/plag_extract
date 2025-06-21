ABC=list(map(int,input().split()))
print("Yes" if min(ABC[0],ABC[1])<ABC[2]<max(ABC[0],ABC[1]) else "No")
