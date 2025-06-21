s = list(input())
len_s= len(s)
#print(s)
if len_s%2==0:
    ans_0=['0','1']*int(len_s/2)
    ans_1=['1', '0']*int(len_s/2)
else:
    ans_0=['0'] + ['1', '0']*int((len_s-1)/2)
    ans_1=['1'] + ['0','1']*int((len_s-1)/2)
    
#print(ans_0)
#print(ans_1)

count_0 =0
for i in range(len_s):
    if ans_0[i] is not s[i]:
        count_0+=1

count_1 =0
for i in range(len_s):
    if ans_1[i] is not s[i]:
        count_1 += 1
print(min(count_0, count_1))