"""
picks : 곡괭이 개수 [dia, iron, stone]
minerals : 광물들의 순서

광물 5개마다 비용 계산
다이아 -> 철 -> 돌 광물 순서대로 광물이 많을 수록 다이아 -> 철 -> 돌 곡괭이 순
"""
def solution(picks, minerals):
    answer = 0
    
    if len(minerals) % 5 == 0:
        iter_num = len(minerals) // 5
    else:
        iter_num = len(minerals) // 5 + 1
        
    mineral_list = []
    for i in range(iter_num):
        if 5*i >= 5*sum(picks):
            continue
        mineral_list.append(minerals[5*i: 5*(i+1)])
        
    # print(mineral_list)

    mineral_num_list = []  # mineral_num[0] : dia, mineral_num[1] : iron, mineral_num[2] : stone
    for i in mineral_list:
        dia = 0
        iron = 0
        stone = 0
        for j in i:
            if j == 'diamond':
                dia += 1
            elif j == 'iron':
                iron += 1
            elif j == 'stone':
                stone += 1
            else:
                break
        mineral_num_list.append([dia, iron, stone])
        
    print(mineral_num_list)
    # mineral_num_list.sort(reverse=True, key=lambda x: x[2])
    # mineral_num_list.sort(reverse=True, key=lambda x: x[1])
    # mineral_num_list.sort(reverse=True, key=lambda x: x[0])
    mineral_num_list.sort(key=lambda x: (-x[0], -x[1], -x[2]))
    print(mineral_num_list)
    
    for i in mineral_num_list:
        if picks[0] > 0:
            answer += i[0] + i[1] + i[2]
            picks[0] -= 1
        elif picks[1] > 0:
            answer += (5 * i[0] + i[1] + i[2])
            picks[1] -= 1
        elif picks[2] > 0:
            answer += (25 * i[0] + 5 * i[1] + i[2])
            picks[2] -= 1
        else:
            break
            
    return answer