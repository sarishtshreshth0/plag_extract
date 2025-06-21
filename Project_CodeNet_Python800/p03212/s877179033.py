def calc(n):
  dic={0:0,1:3,2:5,3:7}
  ret=0
  for j in range(9):
    ret+=dic[n%4]*(10**j)
    n-=n%4
    n//=4
    if n==0:
      return ret

def check(n):
  cnt=[0]*10
  for c in str(n):
    cnt[int(c)]+=1
  if cnt[0]==0 and cnt[3]>=1 and cnt[5]>=1 and cnt[7]>=1:
    return True
  else:
    return False

n=int(input())
arr=[]
for i in range(4**9):
  tmp=calc(i)
  if check(tmp)==True:
    arr.append(tmp)
arr=sorted(arr)
for i in range(len(arr)):
  if arr[i]>n:
    print(i)
    break
else:
  print(len(arr))