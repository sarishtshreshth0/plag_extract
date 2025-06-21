def calc(a, b, c, d) :
  if c < a and b < d :
    return b - a
  elif a <= c <= b : 
    if d < b : 
      return d - c
    else : 
      return b - c
  elif a <= d <= b :
    return d - a
  else : 
    return 0

a, b, c, d = tuple(map(int, input().split()))

print(calc(a, b, c, d))
