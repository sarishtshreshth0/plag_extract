S = list(input())

goal = [str(i%2) for i in range(len(S))]    #完成形１'01010101...'
diff1 = 0 #完成形1'01010101...'と比較したとき、異なる文字の数
diff2 = 0 #完成形2'10101010...'と比較したとき、異なる文字の数

for i in range(len(S)):
    if S[i] != goal[i]:
        diff1 += 1
    else:
        diff2 += 1
        
print(min(diff1,diff2))