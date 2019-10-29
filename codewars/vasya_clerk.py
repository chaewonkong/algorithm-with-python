"""Vasya Clerk

The new "Avengers" movie has just been released! 
There are a lot of people at the cinema box office standing in a huge line. 
Each of them has a single 100, 50 or 25 dollars bill. 
An "Avengers" ticket costs 25 dollars.

Vasya is currently working as a clerk. 
He wants to sell a ticket to every single person in this line.

Can Vasya sell a ticket to each person and give the change 
if he initially has no money and sells the tickets strictly in the order 
people follow in the line?

Return YES, 
if Vasya can sell a ticket to each person 
and give the change with the bills he has at hand at that moment. 
Otherwise return NO.

Examples:
tickets([25, 25, 50]) # => YES 
tickets([25, 100]) # => NO
tickets([25, 25, 50, 50, 100]) # => NO
"""

def tickets(people):
    quarter = 0
    half = 0
    ans = "YES"

    for payment in people:
        if payment == 25:
            quarter += 1
        elif payment == 50:
            quarter -= 1
            half += 1
        else:
            if half > 0:
                half -= 1
                quarter -= 1
            else:
                quarter -= 3
        if quarter < 0:
            ans = "NO"
            
    return ans



    
            


