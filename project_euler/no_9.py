"""Pythagoras Numbers in Python from Project Euler.

For 3 natural number a,b,c (a<b<c)
1. a^2 + b^2 = c^2
2. a + b + c =1000

return a*b*c"""


def pythagoras(N):
	"""Return a*b*c for pythagoras number a,b,c that a+b+c=N"""
	
	for c in range(N//3+1, N-1):
		for b in range(1, c):
			for a in range(1, b):
				if a+b+c ==N and (a**2)+(b**2)==(c**2):	
					return(a*b*c)


print(pythagoras(1000))

