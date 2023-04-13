'''
storey : 현재 층
BFS로 풀 수 있을듯 !
맨 끝 자리 (1의 자리)수부터 생각
e.g. k*100 + j*10 + i
if i > 5:
    roundup이 나음
elif i < 5:
    rounddown이 나음
elif i == 5:
    if j > 5:
        roundup(j)
    elif j < 5:
        roundup(j)
    elif j == 5:
        if k > 5:
            ...
        반복
'''

answer = 0

def asdf(storey):
    global answer
    if storey == 0:
        return
    num = storey % 10
    if num > 5:
        answer += (10 - num)
        storey += 10
    elif num == 5:
        if storey >= 10:
            num2 = (storey // 10) % 10
            if num2 >= 5:
                answer += (10 - num)
                storey += 10
            else:
                answer += num
        else:
            answer += num                
    elif num < 5:
        answer += num
        
    return storey // 10
        
    
    
def solution(storey):
    global answer

    digits = 0
    while True:
        digits += 1
        if storey < 10 ** digits:
            break
    print(digits)
    
    for i in range(digits+1):
        storey = asdf(storey)

    return answer