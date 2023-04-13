"""
최대공약수로 나누면 가장 작은 규칙이 보인다.
"""
import math
def solution(w,h):

    gcd = math.gcd(w, h)
    
    _w = w // gcd
    _h = h // gcd
    
    answer = h*w - (_w + _h - 1) * gcd
    
    return answer