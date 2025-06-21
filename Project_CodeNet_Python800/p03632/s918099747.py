a,b,c,d=map(int,input().split())

def seconds(a,b,c,d):
  if b<=c or d<=a:
    print(0)
    return
  else:
    st=max(a,c)
    go=min(b,d)
    print(go-st)
    return

seconds(a,b,c,d)