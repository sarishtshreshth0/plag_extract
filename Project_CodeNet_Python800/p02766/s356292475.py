n,k =list(map(int,input().split()))

for i in range(31):
  if n < k ** i:
    print(i)
    break