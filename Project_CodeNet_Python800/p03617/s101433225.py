price = [int(x) for x in input().split()];
N = int(input());
price_d = price[3];
price_s = 2*price[2];
price_h = 4*price[1];
price_q = 8*price[0];
p = min([price_q,price_h,price_s]);
if price_d < p :
    if N%2 == 1 :
        ans = (N-1)//2*price_d + p//2;
    else :
        ans = N//2*price_d;
else :
    ans = N*p//2;

print(ans);

