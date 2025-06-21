N = int(input())
count1 = N // 500
count2 = ( N%500 ) // 5
print( 1000*count1 + 5*count2 )
