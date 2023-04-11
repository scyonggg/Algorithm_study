from collections import deque


def solution(sequence, k):
    temp = []

    def mySol(temp):
        acc = 0
        Q = deque()
        for idx, data in enumerate(sequence):
            Q.append((idx, data))
            acc += data
            while acc > k:
                rm = Q.popleft()[1]
                acc -= rm
            if acc == k:
                # print(f'acc : {acc}, k : {k}')
                # print(f'Q : {Q}')
                temp.append([Q[0][0], Q[-1][0]])

    mySol(temp)

    answer = []
    best = 1000000
    for i in temp:
        if (i[1] - i[0]) < best:
            best = i[1] - i[0]
            answer = [i[0], i[1]]

    return answer