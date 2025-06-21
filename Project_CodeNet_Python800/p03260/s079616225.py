A, B = map(int, input().split())

ans = "Yes"
if (A % 2 == 0 or B % 2 == 0):
  ans = "No"

print(ans)
