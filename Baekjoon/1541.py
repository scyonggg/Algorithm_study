S = str(input())  # 입력 문자열

data = []
if '-' in S:
    data = S.split(sep='-')  # data[0] : 더하기, data[1:] : 계산하기
else:
    data.append(S)

if len(data) == 1:  # 수식에 +만 있다
    if '+' in data[0]:
        ss = data[0].split(sep='+')
        res = 0
        for i in ss:
            res += int(i)
        print(res)
    else:
        print(str(data[0]))

else:  # 결론 : sum(data[0]) - sum(data[1:])
    # data[0] 처리
    res1 = 0
    if '+' in data[0]:
        eq = data[0].split(sep='+')
        for i in eq:
            res1 += int(i)
    else:
        res1 += int(data[0])

    res2 = 0
    for i in data[1:]:
        if '+' in i:
            eq = i.split(sep='+')
            for j in eq:
                res2 += int(j)
        else:
            res2 += int(i)

    print(res1 - res2)