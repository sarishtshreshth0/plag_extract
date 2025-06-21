N=int(input())
a=input()
d=[a]
for x in range(N-1):
  b=input()
  if b not in d:
    d.append(b)
    if a[len(a)-1]==b[0]:
      a=b
      if x==N-2:
        print("Yes")
    else:
      print("No")
      break
  else:
    print("No")
    break