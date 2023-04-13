def solution(n):
    answer = ''
    
    div_list = []
    while True:
        n -= 1
        if n >= 3:
            div_list.append(n%3)
        else:
            div_list.append(n)
            break
        n = n // 3
    
    div_list.reverse()
    for i in div_list:
        if i == 0:
            answer += '1'
        elif i == 1:
            answer += '2'
        elif i == 2:
            answer += '4'
    return answer