"""
- 같은 level = 같은 y
- len(nodeinfo) : 1 ~ 10,000
- x, y : 0 ~ 100,000
- 깊이 : ~1,000

- 전위 순회 (preorder)
: 왼쪽부터 DFS

- 후위 순회 (postorder)
: 오른쪽부터 DFS한 후 reverse

"""
import sys
sys.setrecursionlimit(10000)
def find_root(node):
    return max(node, key=lambda x: x[1])
    
def divide_nodes(node, y):
    for i, n in enumerate(node):
        if n[1] == y:
            return node[:i], node[i+1:]
    
def solution(nodeinfo):
    answer = [[]]
    nodes = [[*nodeinfo[i], i+1] for i in range(len(nodeinfo))]
    # nodes.sort(key=lambda x: x[0])
    # nodes.sort(reverse=True, key=lambda x: x[1])
    preorder = []
    postorder = []
    
    def make_tree(node):
        if not node:
            return
        x, y, i = find_root(node)
        preorder.append(i)
        node.sort(key=lambda x: x[0])
        left_node, right_node = divide_nodes(node, y)
        make_tree(left_node)
        make_tree(right_node)
        postorder.append(i)
    
    make_tree(nodes)
    return [preorder, postorder]