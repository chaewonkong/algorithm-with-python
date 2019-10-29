"""Sum of Two Lowest Positive Integers

Create a function that returns the sum of the two lowest positive numbers
 given an array of minimum 4 integers. No floats or empty arrays will be passed.

For example, when an array is passed like [19, 5, 42, 2, 77], the output should be 7.
[10, 343445353, 3453445, 3453545353453] should return 3453455.
"""


def sum_two_smallest_numbers(numbers):
    maximum = 0
    for k in numbers:
        if k > maximum:
            maximum = k
    min_total = maximum * 2
    min_positive = maximum
    for n in numbers:
        if n > 0 and n < min_positive:
            min_positive = n
    for num in numbers:
        if num > min_positive:
            if min_positive + num < min_total:
                min_total = min_positive + num
    return min_total


    
    

