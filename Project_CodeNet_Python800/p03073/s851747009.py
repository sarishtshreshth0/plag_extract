s = input()
ans1 = 0 ; ans2 = 0
for i in range(len(s)) :
    #黒スタートで考える
    if i % 2 == 0 :
        if s[i] != "0" :
            ans1 += 1
    else :
        if s[i] != "1" :
            ans1 += 1

for i in range(len(s)) :
    #白スタートで考える
    if i % 2 == 0 :
        if s[i] != "1" :
            ans2 += 1
    else :
        if s[i] != "0" :
            ans2 += 1
print(min(ans1,ans2))
