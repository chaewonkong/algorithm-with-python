"""뉴스 클러스터링 in Python

2개의 문자열을 입력으로 받고, 각 문자열을 2글자씩 나누어 비교한 뒤, 자카드 유사도를 출력한다.

[입력형식]
입력으로는 str1과 str2의 두 문자열이 들어온다. 각 문자열의 길이는 2 이상, 1,000 이하이다.

입력으로 들어온 문자열은 두 글자씩 끊어서 다중집합의 원소로 만든다. 
이때 영문자로 된 글자 쌍만 유효하고, 기타 공백이나 숫자, 
특수 문자가 들어있는 경우는 그 글자 쌍을 버린다. 
예를 들어 “ab+”가 입력으로 들어오면, “ab”만 다중집합의 원소로 삼고, 
“b+”는 버린다.

다중집합 원소 사이를 비교할 때, 대문자와 소문자의 차이는 무시한다. 
“AB”와 “Ab”, “ab”는 같은 원소로 취급한다.

[출력형식]
입력으로 들어온 두 문자열의 자카드 유사도를 출력한다. 
유사도 값은 0에서 1 사이의 실수이므로, 
이를 다루기 쉽도록 65536을 곱한 후에 소수점 아래를 버리고 정수부만 출력한다.

[예제입출력]
str1   	  str2	       answer
FRANCE	  french	   16384
handshake shake hands  65536
aa1+aa2	  AAAA12	   43690
E=M*C^2	  e=m*c^2	   65536
"""

# process_string() 함수로 앞의 두 함수를 묶어주자
MULTIPLIER = 65536

def adjacent_two_alphabets(st):
    """Return list of all two adjacent letters from arr, 
    removing letter-set with non-alphabet"""

    import string.ascii_lowercase as lowercases
    results = []
    for i in range(len(st) - 1):
        if st[i] in lowercases and st[i+1] in lowercases:
            results.append(st[i] + st[i+1])
    
    return results


def lowercase_without_whitespace(st):
    """Return string only with lowercase"""
#string.whitespace 이용해 refactoring

    st = st.lower()
    filtered_string =""
    results = []

    for i in range(len(st)):
        if st[i] !=" ":
            filtered_string += st[i]

    return filtered_string


def get_jaccard_index(arr1, arr2):
    """Return jaccard index of arr1 and arr2"""
    
    jaccard_index = 1

    if not arr1 and not arr2:
        return jaccard_index

    intersection = []
    union = arr1 + arr2
    # 교집합과 합집합 굳이 실제 구할 필요 없어. 중요한 것은 길이뿐! Refactoring 필요하다
    # Get intersection
    for item in arr1:
        if item in arr2:
            intersection.append(item)

    # Remove intersection from union once
    for inter_item in intersection:
        union.remove(inter_item)
    
    # Get jaccard_index
    jaccard_index = len(intersection)/len(union)
    
    return jaccard_index
        
if __name__ == "__main__":
    str1 = input()
    str2 = input()

    arr1 = adjacent_two_alphabets(lowercase_without_whitespace(str1))
    arr2 = adjacent_two_alphabets(lowercase_without_whitespace(str2))

    print(int(get_jaccard_index(arr1, arr2)*MULTIPLIER))