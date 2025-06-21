# a brute bitch
from bisect import bisect_right
def comb (n,s):
    capt = []; ind = n; 
    stp = n+1; boo = ""
    while bk[0] < 1:
        if bk[ind] < s:
            boo += dip[bk[ind]];
            bk[ind]+=1; 
            if ind + 1 == stp:
                if '7' in boo and '3' in boo and '5' in boo:
                    capt.append(int(boo)); 
                boo = boo[:len(boo)-1];
            ind += 1 if ind + 1 < stp else 0
        else: bk[ind] = 0;ind -= 1; boo = boo[:len(boo)-1]
    return bisect_right(capt,int(val))
val = input()
bk = [0]*(len(val)+1); dip = ['3','5','7']
print(comb(len(val),3))