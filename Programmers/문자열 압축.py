def solution(s):
    result = []
    if len(s) == 1:
        return 1

    for i in range(1, len(s)+1):  # 1개, 2개, ..., len(s)개씩 나누기
        b = ''
        cnt = 1
        tmp = s[:i]
        
        for j in range(i, len(s)+i, i):  # i부터 마지막까지 i개마다 건너뛰며 탐색
            if tmp == s[j: j+i]:  # tmp : 앞 그룹, s[j: j+i] : 현재 그룹
                cnt += 1
            else:
                if cnt != 1:
                    b = b + str(cnt) + tmp
                else:
                    b = b + tmp
                tmp = s[j: j+i]
                cnt = 1
        result.append(len(b))
    
    answer = min(result)
    return answer