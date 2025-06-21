num_list= list(map(int,input().split()))
li_A=list(range(num_list[0],num_list[1]))
li_B=list(range(num_list[2],num_list[3]))

li_C=range(0, 10)
li_A+=li_B

len_1=len(li_A)
len_2=len(set(li_A))
print(len_1-len_2)