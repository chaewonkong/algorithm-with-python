# 전화번호 목록
# https://programmers.co.kr/learn/courses/30/lessons/42577


def solution(phone_book):
    phone_book.sort()
    for i in range(len(phone_book)-1):
        flag = False
        for j in range(len(phone_book[i])):
            if phone_book[i][j] != phone_book[i+1][j]:
                flag = True
                break
        if not flag:
            return flag
    return True


# Test
if __name__ == "__main__":
    T1 = ["119", "97674223", "1195524421"]
    A1 = False
    T2 = ["123", "456", "789"]
    A2 = True

    print(solution(T1) == A1)
    print(solution(T2) == A2)
