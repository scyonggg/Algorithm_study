"""
과제를 끝낸 순서대로 이름을 배열에 담아 return
과제를 하다가 새로운 과제가 생기면 stack에 넣어두기. (가장 최근에 멈춘 과제부터 시작하기 때문)
"""

from collections import deque


def solution(plans):
    answer = []
    for i in plans:  # 시작 시간을 분 단위로 변환
        tmp = i[1].split(':')
        i[1] = int(tmp[0]) * 60 + int(tmp[1])
        i[2] = int(i[2])

    plans.sort(key=lambda x: x[1])  # 시작 시간 순으로 정렬
    print(f"plans : {plans}")

    stack = deque()

    for idx in range(len(plans)):
        if idx == len(plans) - 1:
            stack.append(plans[idx])
            break

        # [0]: 과목명, [1]: 시작 시간, [2]: 걸리는 시간
        A = plans[idx]
        B = plans[idx + 1]

        if A[1] + A[2] < B[1]:  # 다 끝낼 수 있음
            answer.append(A[0])
            time_left = B[1] - (A[1] + A[2])
            while time_left != 0 and stack:
                inter_plan = stack.pop()
                if time_left >= inter_plan[2]:  # 다 할 수 있음
                    answer.append(inter_plan[0])
                    time_left = time_left - inter_plan[2]
                    continue
                else:
                    inter_plan[2] = inter_plan[2] - time_left
                    stack.append(inter_plan)
                    time_left = 0
                    continue
        elif A[1] + A[2] == B[1]:
            answer.append(A[0])
            continue
        else:  # 다 끝낼 수 없음
            A[2] = A[2] - (B[1] - A[1])
            stack.append(A)

    while stack:
        job = stack.pop()
        answer.append(job[0])

    return answer
