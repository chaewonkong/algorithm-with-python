"""Land perimeter

from Codewars
URL: https://www.codewars.com/kata/land-perimeter

Task:
Given an array arr of strings complete the function landPerimeter 
by calculating the total perimeter of all the islands. Each piece of 
land will be marked with 'X' while the water fields are represented as 'O'. 
Consider each tile being a perfect 1 x 1piece of land. 
Some examples for better visualization:

['XOOXO',
 'XOOXO',
 'OOOXO',
 'XXOXO',
 'OXOOO']

 should return: "Total land perimeter: 24", 

while
['XOOO',
 'XOXO',
 'XOXO',
 'OOXX',
 'OOOO']
 should return: "Total land perimeter: 18"
"""

def land_perimeter(arr):
    horizontal = len(arr[0])
    vertical = len(arr)
    ractangles, tangents = 0, 0
    coords = [(i,j) for j in range(horizontal) for i in range(vertical) if arr[i][j] == "X"]
    for i,j in coords:
        ractangles += 1
        sides = [(i-1,j), (i, j-1), (i, j+1), (i+1, j)]
        for x,y in sides:
            if x >= 0 and y >= 0 and x < vertical and y < horizontal and arr[x][y] == "X":
                tangents += 1
    ret = ractangles * 4 - tangents
    return "Total land perimeter: {}".format(ret)


"""Best Solution
land = lambda a: sum(t == ('X', 'X') for r in a for t in zip(r, r[1:])) * 2

def land_perimeter(a):
    return 'Total land perimeter: ' + str(''.join(a).count('X') * 4 - land(a) - land(zip(*a)))
"""