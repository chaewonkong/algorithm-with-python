"""All Balanced Parenthesis

Write a function which makes a list of strings
representing all of the ways you can balance n pairs of parentheses.

ex)
balancedParens(0) => [""]
balancedParens(1) => ["()"]
balancedParens(2) => ["()()","(())"]
balancedParens(3) => ["()()()","(())()","()(())","(()())","((()))"]
"""


'''
def balancedParens(n):
    ans = []

    def generate(parens, opens, closes):
        if opens == n and closes == n:
            ans.append(parens)
            return
        elif opens == n:
            ans.append(parens+")"*(n-closes))
            return
        
        if opens > closes:
            generate(parens + ")", opens, closes + 1)
        generate(parens + "(", opens+1, closes)
    
    generate("", 0, 0)
    return ans
'''

def balancedParens(n):
    ret = []

    def generate(parans, openings, closings):
        if openings == 0 and closings == 0:
            ret.append(parans)
            return
        elif openings == 0:
            ret.append(parans + ")" * closings)
            return
        if openings < closings:
            generate(parans + ")", openings, closings-1)
        generate(parans +"(", openings-1, closings)
    
    generate("", n, n)
    return ret

print(balancedParens(3))
