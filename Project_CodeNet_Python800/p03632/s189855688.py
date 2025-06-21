

a, b, c, d = map(int,input().split())

"""
case1
a b c d   →0

case2
a c b d  → b-c

case3
a c d b → d-c

case4
c a 

start →開始時刻のmax
end →終了時刻のmin



"""
starttime = max(a,c)
endtime  = min(b,d)

if starttime < endtime:
    result  = endtime - starttime
else:
    result = 0




"""
if b<=c :
    result = 0
else:  ## c < b 
    if b < d:  ## c < b < d
        result  = b - c
    else:  ## c < d <= b
        result  = d -c
"""



print(result)

