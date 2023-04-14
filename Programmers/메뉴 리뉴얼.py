from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []
    
    for c in course:  # 코스 메뉴 개수
        tmp = []
        for order in orders:
            comb = combinations(sorted(order), c)
            tmp += comb
        counter = Counter(tmp)
        print(counter)
        if len(counter) != 0 and max(counter.values()) != 1:
            answer += [''.join(f) for f in counter if counter[f] == max(counter.values())]
    
    return sorted(answer)