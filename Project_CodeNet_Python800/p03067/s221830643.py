import math
from datetime import date

def main():
	line = input().split()
	a = int(line[0])
	b = int(line[1])
	c = int(line[2])

	if c >= min(a, b) and c <= max(a, b):
		print("Yes")
	else:
		print("No")

main()
