N,A,B=map(int,input().split())
S=input()

tukasya=0
kaigai=0
for i in range(N):
  if (S[i]=='a' and tukasya<A+B):
    print('Yes')
    tukasya=tukasya+1
  elif S[i]=='b':
    if (kaigai<B and tukasya<A+B):
      print('Yes')
      tukasya=tukasya+1
      kaigai=kaigai+1
    else:
      print('No')
      kaigai=kaigai+1
  else:
    print('No')