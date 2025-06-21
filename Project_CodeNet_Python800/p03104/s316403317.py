a,b=map(int,input().split())
lenb=len(str(bin(b)))-2

#a=2、b=8とする
#0000 0
#0001 1
#0010 2
#0011 3
#0100 4
#0101 5 
#0110 6
#0111 7
#1000
#各桁の1の個数を数えればよさそう
#i桁目のX番目までの１の数
#(x+1)%(2**(i+1))-(2*(i))

result=""

if a!=0:
    a-=1
if a%4 in [1,2]:
    a4="1"
else:
    a4="0"
if b%4 in [1,2]:
    b4="1"
else:
    b4="0"

if a4==b4:
    result="0"
else:
    result="1"

for i in range(1,lenb):
    a4=(max(0,(a+1)%(2**(i+1))-(2**(i))))%2
    b4=(max(0,(b+1)%(2**(i+1))-(2**(i))))%2
    if a4==b4:
        result="0"+result
    else:
        result="1"+result


print(int(result,2))

