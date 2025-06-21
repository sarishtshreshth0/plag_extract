if __name__ == '__main__':
  a,b,c = map(int, input().split())
  if(a>b):
    a,b = b,a
  if(c > a and c < b):
    print("Yes")
  else:
    print("No")