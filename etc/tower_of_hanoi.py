"""Tower Of Hanoi
in Python Algorithm

The Tower of Hanoi is an simple algorithm with three posts
and n number of discs. 
The disks in the start post must be moved to end post
by following rules below.

1. There are n number of stored disks in the start post.
All disks should be moved to the end post.
2. All disks are in different size. At first, from largest to smallest, 
the disks are stored in the start post, bottom to top.
3. The disk can be moved one piece at a time.
4. Only the disk located on top is movable(middle ones are not movable).
5. Only smaller disk can be on top of larger disk(larger one can not be moved 
on top of smaller one).
"""

def tower_of_hanoi(n):
	"""Move all the disks in the tower of hanoi"""

	arr = [[n-i for i in range(n)], [], []]
	print(arr)
	
	def sort_disk(n, start, mid, end):
		"""Move Disks"""

		if n == 1:
			end.append(start.pop())
			return
		else:
			sort_disk(n-1, start, end, mid)
			print(arr)
			end.append(start.pop())
			print(arr)
			sort_disk(n-1, mid, start, end)

	sort_disk(n, arr[0], arr[1], arr[2])

	print(arr)

if __name__ =="__main__":
	tower_of_hanoi(3)