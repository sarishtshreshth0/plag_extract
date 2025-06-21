def main():
 num = list(map(int,input().split()))
 if(num[0]>num[1]):
  if(num[1]!=1):
   print('Alice')
  else:
   print('Bob')
 elif(num[1]>num[0]):
  if(num[0]!=1):
   print('Bob')
  else:
   print('Alice')
 else:
   print('Draw') 

main()
