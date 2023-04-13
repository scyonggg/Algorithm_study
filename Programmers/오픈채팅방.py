def solution(record):
    answer = []
    
    users = {}
    messages = []
    for i in record:
        act = i.split()  # act[0]: 동작(Enter, Leave, Change), act[1]: uid, act[2]: 닉네임
        if act[0] == 'Enter':
            users[act[1]] = act[2]
            messages.append(['Enter', act[1]])
        elif act[0] == 'Leave':
            messages.append(['Leave', act[1]])
        elif act[0] == 'Change':
            users[act[1]] = act[2]

    # print(users, type(users))
    for i in messages:
        if i[0] == 'Enter':
            answer.append(f'{users[i[1]]}님이 들어왔습니다.')
        elif i[0] == 'Leave':
            answer.append(f'{users[i[1]]}님이 나갔습니다.')
            
    return answer