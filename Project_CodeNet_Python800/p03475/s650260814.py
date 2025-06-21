N=int(input())
tmp=[list(map(int,input().split())) for i in range(N-1)]
for i in range(N-1):
   time=0
   for j in range(i,N-1):
      data=tmp[j]
      if time<data[1]:
         time=data[1]+data[0]
      else:
         if time%data[2]==0:
            time+=data[0]
         else:
            time+=data[2]-(time%data[2])+data[0]
   print(time)
print(0)