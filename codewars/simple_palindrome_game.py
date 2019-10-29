"""Simple Palindrome Game

In this Kata, two players, Alice and Bob, are playing a palindrome game. 
Alice starts with string1, Bob starts with string2, 
and the board starts out as an empty string. 
Alice and Bob take turns; during a turn, 
a player selects a letter from his or her string, 
removes it from the string, and appends it to the board; 
if the board becomes a palindrome (of length >= 2), the player wins. 
Alice makes the first move. Since Bob has the disadvantage of playing second, 
then he wins automatically if letters run out or the board is never a palindrome. 
Note also that each player can see the other player's letters.

The problem will be presented as solve(string1,string2). 
Return 1 if Alice wins and 2 it Bob wins.


[examples]
solve("abc","baxy") = 2 
    -- There is no way for Alice to win. 
    If she starts with 'a', Bob wins by playing 'a'. The same case with 'b'. 
    If Alice starts with 'c', 
    Bob still wins because a palindrome is not possible. Return 2.
solve("eyfjy","ooigvo") = 1 
    -- Alice plays 'y' and whatever Bob plays, 
    Alice wins by playing another 'y'. Return 1.
solve("abc","xyz") = 2 
    -- No palindrome is possible, so Bob wins; return 2
solve("gzyqsczkctutjves","hpaqrfwkdntfwnvgs") = 1 
    -- If Alice plays 'g', Bob wins by playing 'g'. 
    Alice must be clever. She starts with 'z'. 
    She knows that since she has two 'z', the win is guaranteed. 
    Note that she also has two 's'. But she cannot play that. Can you see why? 
solve("rmevmtw","uavtyft") = 1 
    -- Alice wins by playing 'm'. Can you see why?
"""

'''
문제 접근 방법: 엘리스가 이길 수 있으면 1을 없으면 2를 반환한다(엘리스가 이기고 지는 것에 따라 밥도 결정되므로)

엘리스가 이기기 위한 방법: 
    1) 같은 글자가 반드시 2개 있어야 한다(시작을 엘리스가 하므로 반드시 끝나는 글자도 엘리스가 내야함)
    2) 그 같은 글자는 밥이 가지고 있지 않아야 한다(아니라면 밥이 바로 그 글자를 내면서 시합 종료)
    3) 만약 bob의 string이 empty라면? 그래도 엘리스는 같은 두 개의 글자를 가져야 함

'''
def solve(str1,str2):
    alice = []
    for c in str1:
        if c in alice and c not in str2:
             return 1
        alice.append(c)
    return 2

