""""Slice m number of letters from offset 0 and paste them to the end of string
"""
'''
def move_letters_to_back(string, m):
    """Move m number of letters from front to back"""

    temp_str = ""
    result = ""
    str_list = [_ for _ in string]

    for i in range(m):
        temp_str += str_list.pop(0)
    
    for letter in str_list:
        result += letter
    result += temp_str

    return  result
'''

'''
def move_letters_to_back(string, m):

    temp_list = [_ for _ in string]

    for i in range(m):
        temp_list.append(temp_list.pop(0))
    
    return "".join(temp_list)
'''

def move_letters_to_back(string, m):

    if m == 0:
        return string

    temp_list = []
    length = len(string)

    for i in range(m, length):
        temp_list.append(string[i])
    for j in range(m):
        temp_list.append(string[j])
    
    return "".join(temp_list)


# Test Block
if __name__ == "__main__":
    string, m = input().split(",")
    m = int(m)
    print(move_letters_to_back(string, m))