"""Count One

Return number of 1 in binary number of decimal input n
"""

# def count_one(decimal):
    
#     binary = ""
#     index = 0
#     count = 0

#     def get_bin(n, binary):
#         if n <= 2:
#             return "1" + binary
#         binary = str(n % 2) + binary
#         return get_bin(n//2, binary)

#     def get_count(binary, index, count):
#         if index == len(binary):
#             return count
#         if binary[index] == "1":
#             count += 1
#         return get_count(binary, index+1, count)
    
#     return get_count(get_bin(decimal, binary), index, count)

def count_one(n):
    return 0 if n == 0 else count_one(n//2) + n % 2


if __name__ == "__main__":
    decimal = int(input())
    target = bin(decimal)
    print(count_one(decimal))