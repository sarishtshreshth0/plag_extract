N = int(input())
w = input()
W_list = [w]
for i in range(N-1):
  W = input()
  if w[-1] == W[0] and W not in W_list:
    W_list.append(w)
    w = W
  else:
    print("No")
    exit()
print("Yes")