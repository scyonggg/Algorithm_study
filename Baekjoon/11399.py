N = int(input())
P = sorted(list(map(int, input().split())))
total_T = 0
for i in range(len(P)):
    total_T += P[i] * (len(P) - i)
print(total_T)