prices = [ int(p) for p in input().split(" ") ]
N = int(input())

total_price = 0

p1 = {"0.25": prices[0],  "0.5": prices[1], "1": prices[2], "2": prices[3]}
p2 = {"0.25": prices[0] * 8,  "0.5":prices[1] * 4, "1":prices[2] * 2, "2":prices[3]}
min_price = sorted(p2.items(), key=lambda x:x[1])

for item in min_price:
  if N >= float(item[0]):
    buy_num = int(N / float(item[0]))
    total_price += p1[item[0]] * buy_num
    N -= int(float(item[0]) * buy_num)
    #print(total_price, buy_num, N)
    
  if N == 0:
    break

print(total_price)
