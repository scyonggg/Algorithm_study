import sys

read = sys.stdin.readline
n = int(read().rstrip())
m = int(read().rstrip())
recommend = list(map(int, read().rstrip().split()))

frame = []
student = {k: 0 for k in range(1, 101)}

def findMin():
    minimum = 1000
    min_idx = 0
    for i in frame:  # 사진틀에 걸려있는 학생 목록.
        if minimum > student[i]:  # 현재 최솟값보다 i번째 학생의 투표 수가 작으면 갱신
            minimum = student[i]
            min_idx = i
    return min_idx  # 사진틀에 걸려 있는 학생 중 추천 수가 가장 작은 학생 번호


for i in recommend:  # 추천 받은 학생
    student[i] += 1  # 추천 받으면 추천 횟수 증가
    if i in frame:  # 이미 사진틀에 게시되어있으면 통과
        continue
    if len(frame) != n:  # 사진틀이 비어있으면 게시
        frame.append(i)
    else:  # 사진틀이 비어있지 않을 때
        min_idx = findMin()  # 사진틀에 있는 학생 중 추천 수가 가장 적은 학생
        frame.remove(min_idx)  # 사진틀에서 삭제
        student[min_idx] = 0  # 추천 횟수 0으로 초기화
        frame.append(i)  # 사진 게시

frame.sort()
for j in frame:
    print(j, end=' ')