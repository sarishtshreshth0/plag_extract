def main():
  x = int(input())
  ans=int(x/500)*1000
  x-=int(x/500)*500
  ans+=int(x/5)*5
  print(ans)

main()