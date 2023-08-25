import heapq


def solution(n, k, enemy):
    answer = 0
    '''
    n : 병사 수
    k : 무적권
    enemy[i] : i+1 라운드의 적의 수
    '''
    total_enemy = sum(enemy)
    past_enemy = []
    # 예외 설정
    if n >= total_enemy:  # 병사 수가 총 적의 수보다 많을 경우
        answer = len(enemy)
        return answer
    elif k >= len(enemy):  # 무적권이 총 라운드 수보다 많을 경우
        answer = len(enemy)
        return answer

    # 무적권 없이 병사만으로 막을 수 있는 라운드의 수
    rounds = 0
    for cur_enemy in enemy:
        # print(f'rounds : {rounds}, heap : {past_enemy}, k : {k}, n : {n}, cur_enemy : {cur_enemy}')
        if n >= cur_enemy:
            n -= cur_enemy
            heapq.heappush(past_enemy, -cur_enemy)
            rounds += 1
        else:
            if k >= 1:
                k -= 1
                if not past_enemy:  # heap이 비었을 때
                    pass
                else:
                    temp = -heapq.heappop(past_enemy)
                    big = max(temp, cur_enemy)
                    small = min(temp, cur_enemy)
                    n += big
                    if n >= cur_enemy:
                        n -= cur_enemy
                        heapq.heappush(past_enemy, -small)
                    else:
                        break
                rounds += 1
            else:
                break
    answer = rounds

    return answer


'''모범 답안'''
# from heapq import heappush, heappop

# def solution(n, k, enemy):
#     answer, sumEnemy = 0, 0
#     heap = []

#     for e in enemy:
#         heappush(heap, -e)
#         sumEnemy += e
#         if sumEnemy > n:
#             if k == 0: break
#             sumEnemy += heappop(heap)
#             k -= 1
#         answer += 1

#     return answer