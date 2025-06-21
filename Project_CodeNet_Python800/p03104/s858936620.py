a,b=map(int,input().split())

def calc(x):
      
    a = x%4

    if a == 0:
        return x
    elif a == 1:
        return 1
    elif a == 2:
       return x^1
    else:
        return 0
 
print(calc(b) ^ calc(a-1))
