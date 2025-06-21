s = input()
s_list = [int(x) for x in list(str(s))]


# 0101010... と変換
sum_1 = 0
# 1010101... と変換
sum_2 = 0

# 0101010...
for i in range(len(s_list)):
    if i % 2 == 0:
        if s_list[i] == 1:
            sum_1 += 1
    else:
        if s_list[i] == 0:
            sum_1 += 1

    
# 1010101...
for i in range(len(s_list)):
    if i % 2 == 0:
        if s_list[i] == 0:
            sum_2 += 1
    else:
        if s_list[i] == 1:
            sum_2 += 1

print(min(sum_1, sum_2))