n = int(input())
word_list = []
flag = True
for i in range(n):
    word = input()
    if word_list == []:
        word_list.append(word)
    else:
        if (word_list[-1][-1] == word[0]) and (word not in word_list):
            word_list.append(word)
        else:
            flag = False
            break
            
if flag:
    print('Yes')
else:
    print('No')