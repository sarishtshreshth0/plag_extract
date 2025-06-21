import itertools

n = input()
ans =0

    
if len(n) < 3:
    ans = 0

else:
    if int('7'*len(n)) <= int(n):
        ans = 3**(len(n))- 3*2**(len(n)) + 3
    elif int('3'*len(n)) > int(n):
        ans = 0
    else:
        con = []
        for i in range(len(n)):
            con.append(0)
        con_num = []
        for i in range(3**len(n)):
            con[-1] +=1
            for j in range(len(n)-1,0,-1):
                if con[j] == 3:
                    con[j-1] +=1
                    con[j] = 0
            if con[0] == 0:
                b = '3'
            elif con[0] == 1:
                b= '5'
            elif con[0] == 2:
                b = '7'
            for j in range(1,len(n)):
                if con[j] == 0:
                    a = '3'
                elif con[j] == 1:
                    a = '5'
                elif con[j] == 2:
                    a = '7'
                b += a
            c = list(b)
            if c.count('3') != 0 and c.count('5') != 0 and c.count('7') != 0 and len(b) == len(n):
                con_num.append(int(b))
        for i in range(len(con_num)):
            if int(n) >= con_num[i]:
                ans +=1
    for i in range(3,len(n)):
        ans += 3**(i)- 3*2**(i) + 3
    

print(ans)