"""File Name Sort Algorithm

파일명은 크게 HEAD, NUMBER, TAIL의 세 부분으로 구성된다.

1. HEAD는 숫자가 아닌 문자로 이루어져 있으며, 최소한 한 글자 이상이다.
2. NUMBER는 한 글자에서 최대 다섯 글자 사이의 연속된 숫자로 이루어져 있으며, 
    앞쪽에 0이 올 수 있다. 0부터 99999 사이의 숫자로, 00000이나 0101 등도 가능하다.
3. TAIL은 그 나머지 부분으로, 여기에는 숫자가 다시 나타날 수도 있으며, 아무 글자도 없을 수 있다.

파일은 다음과 같은 방식으로 정렬한다.

1. 파일명은 우선 HEAD 부분을 기준으로 사전 순으로 정렬한다. 
    이때, 문자열 비교 시 대소문자 구분을 하지 않는다. 
    MUZI와 muzi, MuZi는 정렬 시에 같은 순서로 취급된다.
2. 파일명의 HEAD 부분이 대소문자 차이 외에는 같을 경우, NUMBER의 숫자 순으로 정렬한다. 
    9 < 10 < 0011 < 012 < 13 < 014 순으로 정렬된다. 
    숫자 앞의 0은 무시되며, 012와 12는 정렬 시에 같은 같은 값으로 처리된다.
3. 두 파일의 HEAD 부분과, NUMBER의 숫자도 같을 경우, 원래 입력에 주어진 순서를 유지한다. 
    MUZI01.zip과 muzi1.png가 입력으로 들어오면, 
    정렬 후에도 입력 시 주어진 두 파일의 순서가 바뀌어서는 안 된다.

[입력]
1. 배열 files가 주어진다.
2. files는 1000 개 이하의 파일명을 포함하는 문자열 배열이다.
3. 각 파일명은 100 글자 이하 길이로, 영문 대소문자, 숫자, 공백(“ “), 마침표(“.”), 
    빼기 부호(“-“)만으로 이루어져 있다. 파일명은 영문자로 시작하며, 
    숫자를 하나 이상 포함하고 있다.
4. 중복된 파일명은 없으나, 
    대소문자나 숫자 앞부분의 0 차이가 있는 경우는 함께 주어질 수 있다. 
    (muzi1.txt, MUZI1.txt, muzi001.txt, muzi1.TXT는 함께 입력으로 주어질 수 있다.)

[출력]
기준에 따라 정렬된 배열을 출력한다.

[입출력 예제]
입력: [“img12.png”, “img10.png”, “img02.png”, “img1.png”, “IMG01.GIF”, “img2.JPG”]
출력: [“img1.png”, “IMG01.GIF”, “img02.png”, “img2.JPG”, “img10.png”, “img12.png”]

입력: [“F-5 Freedom Fighter”, “B-50 Superfortress”, “A-10 Thunderbolt II”, “F-14 Tomcat”]
출력: [“A-10 Thunderbolt II”, “B-50 Superfortress”, “F-5 Freedom Fighter”, “F-14 Tomcat”]
"""

def is_first_item_smaller(file_a, file_b, names):
    """Return boolean results for a < b"""

    def destructure_file(filename):
        """Return list contains head, number, tail from given filename"""

        head = ""
        number = ""
        tail = ""
        i = 0
        head_end = 0
        while i < len(filename):
            if filename[i].isnumeric():
                head = filename[:i]
                head_end = i
                break
            i += 1
        
        initial_i = i
        while i < len(filename):
            if not filename[i].isnumeric() or i - initial_i > 5:
                number = filename[head_end:i]
                tail = filename[i:]
                break
            i += 1
        
        return head, number, tail
    
    processed_a, processed_b = destructure_file(file_a), destructure_file(file_b)

    # Compare heads
    if processed_a[0].lower() < processed_b[0].lower():
        return True
    elif processed_a[0].lower() > processed_b[0].lower():
        return False
    # Compare numbers
    elif int(processed_a[1]) < int(processed_b[1]):
        return True
    elif int(processed_a[1]) > int(processed_b[1]):
        return False
    # Compare Indexes
    else:
        index_a, index_b = 0, 0
        for i in range(len(names)):
            if names[i] == file_a:
                index_a = i
            elif names[i] == file_b:
                index_b = i
        if index_a < index_b:
            return True
        else:
            return False
    
   
def merge_sort_files(names):
    """Sort files in names array by using merge sort
    and is_first_item_smaller function"""

    def divide(lo, hi):

        mid = (lo + hi) // 2
        if lo == hi:
            return
        else:
            divide(lo, mid)
            divide(mid+1, hi)
            merge(lo, mid, hi)
    
    def merge(lo, mid, hi):
        
        left = lo
        right = mid + 1
        temp = []
        while left <= mid or right <= hi:
            if left <= mid and (right > hi or is_first_item_smaller(names[left], names[right], names)):
                temp.append(names[left])
                left += 1
            else:
                temp.append(names[right])
                right += 1       
        names[lo:hi+1] = temp

    divide(0, len(names)-1)
    return names


# Test block
if __name__ == "__main__":
    #Test Cases
    names1 = ['img12.png', 'img10.png', 'img02.png', 'img1.png', 'IMG01.GIF', 'img2.JPG']
    names2 = ['F-5 Freedom Fighter', 'B-50 Superfortress', 'A-10 Thunderbolt II', 'F-14 Tomcat']

    # Print Results
    print("Test1: ", merge_sort_files(names1))
    print("Test2: ", merge_sort_files(names2))