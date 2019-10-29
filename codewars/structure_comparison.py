""" Nesting Structure Comparison

Complete the function/method (depending on the language) to return true/True 
when its argument is an array that has the same nesting structure as the first array.

[example]
# should return True
same_structure_as([ 1, 1, 1 ], [ 2, 2, 2 ] )
same_structure_as([ 1, [ 1, 1 ] ], [ 2, [ 2, 2 ] ] )

# should return False 
same_structure_as([ 1, [ 1, 1 ] ], [ [ 2, 2 ], 2 ] )
same_structure_as([ 1, [ 1, 1 ] ], [ [ 2 ], 2 ] )

# should return True
same_structure_as([ [ [ ], [ ] ] ], [ [ [ ], [ ] ] ] )

# should return False
same_structure_as([ [ [ ], [ ] ] ], [ [ 1, 1 ] ] )
"""


def same_structure_as(original, other):
    if type(original) == list and type(other) == list:
        if len(original) != len(other):
            return False
        for i in range(len(original)):
            if not same_structure_as(original[i], other[i]):
                return False
        return True
    elif type(original) == list or type(other) == list:
        return False
    else:
        return True
