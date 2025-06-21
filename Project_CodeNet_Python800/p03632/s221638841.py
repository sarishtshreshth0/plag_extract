def main():
  a,b,c,d = list(map(int,input().split()))
  if b <=c or d <= a:
    print(0)
  elif a<=c and d<=b:
    print(d-c)
  elif c<=a and b<=d:
    print(b-a)
  elif b <d:
    print(b-c)
  else:
    print(d-a)
    
main()