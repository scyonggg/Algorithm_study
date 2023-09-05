import sys
def solution(sequence, k):
    answer = []
    num_words = len(sequence)

    pl = 0
    pr = 0
    shortest = sys.maxsize
    cur = sequence[pl]
    while pl < num_words:
        if cur < k:
            if pr < num_words-1:
                pr += 1
                cur += sequence[pr]
            else:
                cur -= sequence[pl]
                pl += 1
        elif cur > k:
            cur -= sequence[pl]
            pl += 1
        else:
            if pr - pl < shortest:
                shortest = pr - pl
                answer = [pl, pr]
            cur -= sequence[pl]
            pl += 1
            
    
    return answer

# from collections import deque

# def solution(sequence, k):
#     temp = []
#     def mySol(temp):
#         acc = 0
#         Q = deque()
#         for idx, data in enumerate(sequence):
#             Q.append((idx, data))
#             acc += data
#             while acc > k:
#                 rm = Q.popleft()[1]
#                 acc -= rm
#             if acc == k:
#                 # print(f'acc : {acc}, k : {k}')
#                 # print(f'Q : {Q}')
#                 temp.append([Q[0][0], Q[-1][0]])
#     mySol(temp)
    
#     answer = []
#     best = 1000000
#     for i in temp:
#         if (i[1] - i[0]) < best:
#             best = i[1] - i[0]
#             answer = [i[0], i[1]]
    
#     return answer