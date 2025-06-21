n=int(input())-1
tmp=input()
wordset={tmp}
#print(wordset)
for i in range(n):
  w=input()
  if w in wordset or w[0]!=tmp[-1]:
    print('No')
    exit()
  else:
    wordset=wordset|{w}
    tmp=w
  #print(wordset)
print('Yes')
