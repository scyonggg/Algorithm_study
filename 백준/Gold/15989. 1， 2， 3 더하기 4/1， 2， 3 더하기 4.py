T = int(input())
for t in range(T):
    n = int(input())
    cnt = 0

    l3 = n // 3
    for l in range(l3, -1, -1):
        nn = n - 3 * l
        l2 = nn // 2
        cnt += l2 + 1

    print(cnt)
