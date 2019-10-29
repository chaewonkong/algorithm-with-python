"""Sum of Intervals

Write a function called sumIntervals/sum_intervals() 
that accepts an array of intervals, 
and returns the sum of all the interval lengths. 
Overlapping intervals should only be counted once.

Intervals
Intervals are represented by a pair of integers in the form of an array. 
The first value of the interval will always be less than the second value. 
Interval example: [1, 5] is an interval from 1 to 5. 
The length of this interval is 4.

Overlapping Intervals
List containing overlapping intervals:

[
   [1,4],
   [7, 10],
   [3, 5]
]

(examples)
sumIntervals( [
   [1,2],
   [6, 10],
   [11, 15]
] ); // => 9

sumIntervals( [
   [1,4],
   [7, 10],
   [3, 5]
] ); // => 7

sumIntervals( [
   [1,5],
   [10, 20],
   [1, 6],
   [16, 19],
   [5, 11]
] ); // => 19
"""


def sum_of_intervals(intervals):
    container = set()
    for start, end in intervals:
        for n in range(start, end):
            container.add(n)
    return len(container)

# print(sum_of_intervals([(1, 5), (1, 5)]))
# print(sum_of_intervals([(1, 4), (7, 10), (3, 5)]))
# print(sum_of_intervals([[1,5],[10, 20], [1, 6],[16, 19],[5, 11]]))