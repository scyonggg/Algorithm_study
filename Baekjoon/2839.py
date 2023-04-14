N = int(input())

def solution():
    for i in reversed(range(N//5 + 1)):
        a = N - 5 * i
        if a == 0:
            print(i)
            return
        for j in reversed(range(a//3+1)):
            b = a - 3 * j
            if b == 0:
                print(i + j)
                return
    print(-1)
    return

solution()
