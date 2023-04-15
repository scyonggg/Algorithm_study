''' Note
len(routes) : 1 ~ 10,000
routes[0], routes[1] : -30,000 ~ 30,000
routes[0] : 진입
routes[1] : 진출

< 풀이 >
현재 차량 A, 다음 차량 B에 대해서 경우의 수는 3가지이다.
1) A와 B가 겹치는 구간이 없는 경우 -> A, B 각각 한 대씩
2) A와 B의 진출,진입이 동일 -> 진출=진입 구간에 카메라 하나로 해결
3) A와 B의 진출, 진입이 겹치는 구간 존재
    3-1) A 진출 <= B 진출
    
    3-2) A 진출 > B 진출
-> B[1] = A[1]으로 바꾼 뒤, A=B, B=B+1 식으로 계속 가기.


'''
def solution(routes):
    answer = 0

    # print(routes)
    routes.sort(key=lambda x: x[1])
    # print(routes)
    
    cursor = 0
    while cursor < len(routes):  # routes[cursor][0] : 시작, routes[cursor][1] : 끝
        if cursor == len(routes)-1:
            answer += 1
            return answer
        ncursor = cursor + 1
        while routes[ncursor][0] <= routes[cursor][1]:  # cursor 끝보다 빨리 시작하면 잇는다.
            if ncursor == len(routes) - 1:
                answer += 1
                return answer
            ncursor += 1
        answer += 1
        cursor = ncursor
    
        
    return answer