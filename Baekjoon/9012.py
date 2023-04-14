import sys
from collections import deque

read = sys.stdin.readline

T = int(input())
S = []
for _ in range(T):
    S.append(str(read().rstrip()))

for idx, s in enumerate(S):
    valid = True
    stack = deque()
    if s[-1] == '(':
        print('NO')
        continue
    for i in s:
        if i == '(':
            stack.append(i)
        elif i == ')':
            if not '(' in stack:
                valid = False
                break
            stack.pop()
    if stack:
        valid = False
    if valid:
        print('YES')
    else:
        print('NO')
