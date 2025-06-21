A, B = map(int, input().split())
n = 2
answer = ((B+1)//2-A//2)%2
A -= 1
while n <= B:
  cnt_b = 0
  if (B//n)%2 != 0:
    cnt_b += B%n
  cnt_b += B//n
  cnt_a = 0
  if (A//n)%2 != 0:
    cnt_a += A%n
  cnt_a += A//n
  if (cnt_b-cnt_a)%2 != 0:
    answer += n
  n *= 2
print(answer)
  
