import sys

read = sys.stdin.readline
N, M = map(int, read().rstrip().split())

city = []  # N*N
house = []  # 살아남은 치킨집
chickens = []  # 원래 치킨집. 길이 = b
for i in range(N):
    data = list(map(int, read().rstrip().split()))
    city.append(data)
    for idx, j in enumerate(data):
        if j == 1:  # 집
            house.append([i, idx])  # i행 j열 위치 삽입
        elif j == 2:  # 치킨집
            chickens.append([i, idx])  # i행 j열 위치 삽입

w = len(chickens)
answer = []
distances = []

def back_tracking(cnt, idx):
    # M개의 치킨집을 선택했을 때
    if cnt == M:
        distance = 0  # 도시의 치킨 거리
        for n, m in house:  # a개의 가정집 반복문
            minimum_house = 12345  # 집의 치킨 거리
            for a, b in answer:  # 선택한 M개의 치킨집 반복문
                temp = ChickenDistance(n, m, a, b)
                if minimum_house > temp:
                    minimum_house = temp
            distance += minimum_house
        distances.append(distance)
        return

    # 반복문을 통해 w까지 돌기.
    for i in range(idx, w):
        answer.append(chickens[i])  # 치킨집 위치 (i행 j열)
        back_tracking(cnt + 1, i + 1)
        answer.pop()
    return

def ChickenDistance(x1, y1, x2, y2):
    return abs(x2-x1) + abs(y2-y1)

back_tracking(0, 0)
print(min(distances))
