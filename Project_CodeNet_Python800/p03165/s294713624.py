from copy import copy

def getval():
    s = input()
    t = input()
    return s,t

def main(s,t):
    dp = ["" for i in range(len(t)+1)]
    for i in range(len(s)):
        temp = [""]
        for j in range(len(t)):
            prev = dp[j+1]
            last = temp[-1]
            if len(prev)>len(last):
                temp.append(prev)
            elif len(prev)<len(last):
                temp.append(last)
            elif s[i]==t[j]:
                temp.append("".join([dp[j],s[i]]))
            else:
                temp.append(prev)
        dp = copy(temp)
        
    print(dp[len(t)])
                    
if __name__=="__main__":
    s,t = getval()
    main(s,t)