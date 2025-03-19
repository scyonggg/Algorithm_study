"""
len(words) = N : 2 ~ 100,000
전체 단어 길이 = L : 2 ~ 1,000,000

a b c d e f g h i j
k l m n o p q r s t
u v w x y z

총 26개.
"""

class Node:
    def __init__(self, word: str):
        self.data = word
        self.num_visited = 1  # 저장하면서 이 노드를 방문한 횟수.
        self.children = {}  # {w: Node}

def solution(words):
    answer = 0
    
    root = Node('!')
    for word in words:
        p = root
        for w in word:
            if w in p.children.keys():
                p.children[w].num_visited += 1
            else:
                p.children[w] = Node(w)
            p = p.children[w]
    
    for word in words:
        p = root
        for w in word:
            answer += 1
            p = p.children[w]
            if p.num_visited == 1:
                break
            
    return answer