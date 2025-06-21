s=[*input()];n=len(s);t=['1' if i%2==0 else '0' for i in range(n)]
r=[i==j for i,j in zip(s,t)];print(min(sum(r),n-sum(r)))