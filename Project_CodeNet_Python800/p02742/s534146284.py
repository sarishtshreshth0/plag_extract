h, w = map(int, input().split())
import math
if h == 1 or w == 1:
  print(1)
  
elif h%2 == 0 and w%2 == 0:
  print(h * w // 2)
  
elif h%2 == 0 or w%2 == 0:
  if h%2 == 0:
    we = w//2
    wo = math.ceil(w/2)
    print(we * h//2 + wo * h//2)
    
  else:
    he = h//2
    ho = math.ceil(h/2)
    print(ho * w//2 + he * w//2)

else:
  	# odd
	we = w//2
	wo = math.ceil(w/2)
	he = h//2
	ho = math.ceil(h/2)
	print(ho * wo + he * we)
    
  
  