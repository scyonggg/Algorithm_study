import math

def solution(n, s):
    answer = []
    d, m = s // n, s % n
    if d == 0:
        return [-1]
    if m == 0:
        return [d] * n
    else:
        return [d] * (n-m) + [d+1] * m
    return answer