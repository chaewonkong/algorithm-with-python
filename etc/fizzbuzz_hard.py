"""FizzBuzzz Harder Version

User defined FizzBuzz.

[Input]
Fizzbuzz numbers are given in the first line, divided by white spaces.
Nicknames are given in the second line, same order of Fizzbuzz numbers.
Integer number N is given in the Third line.

[Output]
If N is one of Fizzbuzz numbers, print nicknames, else print N.

[Ex Input]
3 5 7 11
fizz buzz sizz jazz
33

[Ex Output]
fizzjazz
"""

def fizzbuzz_hard(N, nums=(3,5), words=('fizz', 'buzz')):
    """Return words if N is fizzbuzz number, else return N"""

    result = ""
    index = 0
    def calc(index, result):

        # 탈출조건
        if index >= len(nums):
            return N if not result else result
        
        div = nums[index]
        if N % div == 0:
            return calc(index + 1, result + words[index])
        else:
            return calc(index + 1, result)
    return calc(index, result)
    
    

if __name__ == "__main__":
    nums = [int(i) for i in input().split(" ")]
    words = [j for j in input().split(" ")]
    N = int(input())
    print(fizzbuzz_hard(N, nums, words))
    

