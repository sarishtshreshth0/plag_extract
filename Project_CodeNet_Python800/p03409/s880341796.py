def main():
  n = int(input())
  R = [list(map(int, input().split())) for _ in range(n)]
  B = [list(map(int, input().split())) for _ in range(n)]
  
  R = sorted(R, key=lambda p:p[1], reverse=True)
  B = sorted(B)
  ans = 0
  
  for xB, yB in B:
    for xR, yR in R:
      if xR < xB and yR < yB:
        R.remove([xR, yR])
        ans += 1
        break
  print(ans)

if __name__=="__main__":
  main()