'''Note
< 문제 >
바로 앞,뒤 번호 학생에게만 빌려줄 수 있다.
총 학생 수 : 2명 ~ 30명
도난 학생 수 : 1 ~ n명
여벌 학생 수 : 1 ~ n명
여벌 학생도 도난당할 수 있음.

'''
def solution(n, lost, reserve):
    answer = 0
    
    lost.sort()
    reserve.sort()

    # 여벌 체육복이 있는 학생이 도난당할 경우, lost와 reserve 배열에서 제외.
    rm_idx = []
    for i in lost:
        if i in reserve:
            rm_idx.append(i)
    for i in rm_idx:
        lost.remove(i)
        reserve.remove(i)

    # 체육복 도난당한 학생 : 1명, 여벌 체육복 : 1명
    for i in reserve:
        if i-1 in lost:
            lost.remove(i-1)
        elif i+1 in lost:
            lost.remove(i+1)

    answer = n - len(lost)
    return answer