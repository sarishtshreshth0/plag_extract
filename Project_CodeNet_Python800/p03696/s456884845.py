input();s=t=input()
while'()'in t:t=t.replace('()','')
c=t.count;print('('*c(')')+s+')'*c('('))