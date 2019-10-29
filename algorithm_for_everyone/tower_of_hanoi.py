"""Tower of Hanoi Algorithm in Python

1. There are three pillars; 
	One with n number of disks and others with no disks.'
2. All disks are different in it's size.
3. Every disk should be moved to end-point pillar 
	from start-point pillar.
4. You can move one disk at a time.
5. At any case, larger disk cannot be moved atop of smaller disk.
"""


number = int(input("Desired number of disks -->"))


def hanoi(n, start, end, mid):

	if n==1:
		print(start, '->', end)
		return

	# move n-1 number of disks to mid
	hanoi(n-1, start, mid, end)

	# print each move
	print(start, '->', end)

	# move n-1 number of disks from mid to end
	hanoi(n-1, mid, end, start)

hanoi(number, 'start', 'end', 'mid')
