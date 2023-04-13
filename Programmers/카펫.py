'''Note
1. 약수 찾기
    1-1.
        brown = ((w-1)+(h-1))*2  # 2 * (w + h - 2)
        yellow = (w-2)*(h-2)  # (w - 2) * (h - 2)
    1-2.
        w + h = brown // 2 + 2
        wh = yellow + brown
2. 약수 조합에서 덧셈 조건이 맞는 것을 찾기
'''
import math
def solution(brown, yellow):
    answer = []

    # 약수 찾기
    def yaksu(num: int):
        ret = []
        for i in range(1, math.floor(math.sqrt(num))+1):
            if num % i == 0:
                    ret.append([num // i, i])
        print(f'{num} 약수 : {ret}')
        return ret
    
    print(f'yellow + brown : {yellow + brown}')
    common_divisor = yaksu(yellow + brown)
    for i in common_divisor:
        w, h = i[0], i[1]
        if w + h == brown // 2 + 2:
            return [w, h]
    
    return []