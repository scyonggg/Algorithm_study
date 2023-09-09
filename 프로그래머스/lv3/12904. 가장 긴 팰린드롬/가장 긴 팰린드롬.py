def solution(s):
    answer = 0
    def longest_palindrom(s):
        for i in range(len(s),0,-1):
            for j in range(len(s)-i+1):
                if s[j:j+i] == s[j:j+i][::-1]:
                    return i
                
    answer = longest_palindrom(s)
    return answer
# def solution(s):
#     answer = 1

#     len_s = len(s)
#     if len_s == 1:
#         return 1
    
#     def search(left, right):
#         cnt = 0
#         while left >= 0 and right < len(s):
#             left_string = s[left]
#             right_string = s[right]
    
#             if left_string == right_string:
#                 cnt += 1
#                 left -= 1
#                 right += 1
#             else:
#                 break
#         return cnt * 2
    
#     for i in range(len_s-1):
#         # if len_s % 2 == 0:
#         #     answer = max(answer, search(i, i+1))
#         #     # answer = max(answer, search(len_s//2 - 1, len_s//2))
#         # else:
#         #     answer = max(answer, search(i, i+2) + 1)
#         #     # answer = max(answer, search(len_s//2, len_s//2 + 1) + 1)
#         answer = max(answer, search(i, i+1), search(i, i+2) + 1)
    
#     return answer