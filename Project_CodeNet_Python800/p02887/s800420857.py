N = int(input())
slimes = input()

count = 1
current = None

for s in slimes:
  if current is None:
    current = s
    next
  if current != s:
    count +=1
  current = s
    
print(count)

