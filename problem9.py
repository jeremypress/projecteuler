import math
def problem9():
	#Only need to iterate through a and b as c can be derived
	a = 0 
	b = 0
	for a in range(1, 1000):
		for b in range(1, 1000):
			c = math.sqrt(a**2 + b**2)
			if (a + b + c == 1000):
				return a * b * c