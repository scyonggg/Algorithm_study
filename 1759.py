##################################
##### Solution using combinations
##################################
# import sys
# from itertools import permutations, combinations

# read = sys.stdin.readline
# L, C = map(int, read().rstrip().split())

# password = sorted(list(map(str, read().rstrip().split())))
# V = ['a', 'e', 'i', 'o', 'u']

# tuple_perm = combinations(password, L)

# perm = []
# for passwd in tuple_perm:
#     perm.append(list(passwd))
# perm = sorted(perm)
# new_perm = []

# for _perm in perm:
#     cnt = 0  # 모음의 개수
#     for i in V:
#         if i in _perm:
#             cnt += 1
#     if not (cnt < 1 or L - cnt < 2):
#         new_perm.append(_perm)

# new_perm = sorted(new_perm)
# for i in new_perm:
#     myList = []
#     myStr = ""
#     for j in i:
#         myList.append(j)
#     sortedList = sorted(myList)
#     for k in sortedList:
#         myStr += k
#     print(myStr)

##################################
##### Solution using back-tracking
##################################
import sys

read = sys.stdin.readline
L, C = map(int, read().rstrip().split())
words = sorted(list(map(str, read().rstrip().split())))

def back_tracking(cnt, idx):
    # 길이 L의 암호를 만들었을 때
    if cnt == L:
        # 모음, 자음 체크
        vo, co = 0, 0
        for i in range(L):
            if answer[i] in consonant:
                vo += 1
            else:
                co += 1
        if vo >= 1 and co >= 2:
            print("".join(answer))
            
        return

    # 반복문을 통해 암호를 만든다. 다음 idx부터 C까지 back tracking 수행
    for i in range(idx, C):
        answer.append(words[i])
        back_tracking(cnt + 1, i + 1)
        answer.pop()

consonant = ['a', 'e', 'i', 'o', 'u']
answer = []
back_tracking(0, 0)
