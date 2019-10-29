"""Valid Parenthesis

Write a function called that takes a string of parentheses, 
and determines if the order of the parentheses is valid. 
The function should return true if the string is valid, and false if it's invalid.

"()"              =>  true
")(()))"          =>  false
"("               =>  false
"(())((()())())"  =>  true

0 <= input.length <= 100

Along with opening (() and closing ()) parenthesis, 
input may contain any valid ASCII characters. 
urthermore, the input string may be empty and/or not contain any parentheses at all. 
Do not treat other forms of brackets as parentheses (e.g. [], {}, <>).
"""

def valid_parentheses(string):

    parens = [s for s in string if s in ["(", ")"]]
    N = len(parens)
    if N % 2 != 0:
        return False
    elif not parens:
        return True
    opens = 0
    for p in parens:
        if p == "(":
            opens += 1
        else:
            if opens > 0:
                opens -= 1
            else:
                return False
    if opens:
        return False
    return True
    

print(valid_parentheses("hi(hi)()"))