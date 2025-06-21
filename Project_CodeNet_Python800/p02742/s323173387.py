line = input()
data = line.split()
 
height = int(data[0])
wei = int(data[1])

if height !=1 and wei !=1: 
  if height %2 ==0:
    if wei %2 ==0:
      print(int(wei/2)*height)
    else:
      print(int(wei/2)*height+int(height/2))
  else:
    if wei %2 ==0:
      print(int(height/2)* wei + int(wei/2))
    else:
      print(wei* int(height/2) + int(wei/2)+1)
else:
  print(1)