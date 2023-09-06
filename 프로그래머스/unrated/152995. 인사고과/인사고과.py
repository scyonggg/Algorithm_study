'''
scores[0] : 근무 태도 점수
scores[1] : 동료 평가 점수
'''
def solution(scores):
    answer = 0

    w = scores[0]
    wa, wb = w[0], w[1]
    wsum = wa+wb
    
    # scores.sort(key=lambda x:x[1])
    # scores.sort(key=lambda x:x[0], reverse=True)
    scores.sort(key=lambda x: (-x[0], x[1]))
    
    maxb = 0
    for score in scores:
        a, b = score
        if wa < a and wb < b:
            return -1

        if b >= maxb:
            maxb = b
            if a + b > wsum:
                answer += 1
        
        
    return answer + 1