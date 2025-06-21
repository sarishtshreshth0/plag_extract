#-*-coding:utf-8-*-
import sys
input=sys.stdin.readline

def main():
    quota,half,single,double = map(int,input().split())
    want_icetea=int(input())
    cost_list = [4 * quota, 2 * half, single, double / 2]
    ans=0
    if want_icetea >= 2:
        idx1 = cost_list.index(min(cost_list))
        if idx1 == 0:
            ans = 4 * quota * want_icetea
        elif idx1 == 1:
            ans = 2 * half * want_icetea
        elif idx1 == 2:
            ans = single * want_icetea
        elif idx1 == 3:
            if want_icetea % 2 == 0:
                ans = want_icetea // 2 * double
            elif want_icetea % 2 == 1:
                ans = want_icetea // 2 * double
                idx2 = cost_list.index(min(cost_list[:3]))
                if idx2 == 0:
                    ans += 4 * quota
                elif idx2 == 1:
                    ans += 2 * half
                elif idx2 == 2:
                    ans += single
    else:
        idx2 = cost_list.index(min(cost_list[:3]))
        if idx2 == 0:
            ans = 4 * quota * want_icetea
        elif idx2 == 1:
            ans = 2 * half * want_icetea
        elif idx2 == 2:
            ans = single * want_icetea
    print(ans)
if __name__=="__main__":
    main()