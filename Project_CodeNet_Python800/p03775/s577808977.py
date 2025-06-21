n=int(input())
sq=int(n**0.5)
while n%sq!=0:
  sq-=1
print(max(len(str(n//sq)),len(str(sq))))