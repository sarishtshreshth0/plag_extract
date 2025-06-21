a,b,c = map(int, input().split())

if a < b :
  ans = 'Yes' if a < c and c < b else 'No'

if a > b :
  ans =  'Yes' if b < c and c < a else 'No'

print(ans)