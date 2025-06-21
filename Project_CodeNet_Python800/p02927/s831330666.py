'''
 Author: fuad Ashraful Mehmet
 University of Asia Pacific
 created :30 Aug 2019 7.33 PM
 Category :   from Atcoder
 Problem:https: 
'''
import math



m,d=map(int,input().split())



mySet=list()



for i in range(22,d+1):
	res=int(i/10)*(i%10)
	x=int(i/10)

	 
	if res<=m and x>1 and (i%10)>1:
		mySet.append(res)

		# print('{} {}'.format(int(i/10),i%10))




print(len(mySet))