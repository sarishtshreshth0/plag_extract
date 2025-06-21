N = int(input())

words_list = [input()]
c = 1

for i in range(1,N):
    new_word = input()
    words_list.append(new_word)
    
    if new_word in words_list[:i-1]:
        c += 0
        
    elif new_word[0] != words_list[i-1][len(words_list[i-1])-1]:
        c += 0
        
    else:
        c += 1

if c == N:
    print("Yes")
else:
    print("No")