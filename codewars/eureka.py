"""Take a Number And Sum Its Digits Raised To The Consecutive Powers And ....¡Eureka!!

from CodeWars
URL: https://www.codewars.com/kata/5626b561280a42ecc50000d1/train/python

The number 89 is the first integer with more than one digit 
that fulfills the property partially introduced in the title of this kata. 
What's the use of saying "Eureka"? Because this sum gives the same number.

In effect: 89 = 8^1 + 9^2

The next number in having this property is 135.

See this property again: 135 = 1^1 + 3^2 + 5^3

We need a function to collect these numbers, that may receive two integers a, b 
that defines the range [a, b] (inclusive) and outputs a list of the sorted numbers 
in the range that fulfills the property described above.

Let's see some cases:
sum_dig_pow(1, 10) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
sum_dig_pow(1, 100) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 89]
"""

'''def sum_dig_pow(a, b):
    ret = []

    for number in range(a, b+1):
        n = number
        temp = [n%10]
        while n >= 10:
            n //= 10
            temp.append(n % 10)
        idx = len(temp) -1
        total = 0
        for i in range(1, len(temp)+1):
            total += temp[idx] ** i
            idx -= 1
        if total == number:
            ret.append(number)
    return ret
'''

def sum_dig_pow(a, b):
    
    def isAnswer(n):
        return sum([int(d) ** (i+1)  for i, d in enumerate(str(n))]) == n
    
    return [num for num in range(a, b+1) if isAnswer(num)]