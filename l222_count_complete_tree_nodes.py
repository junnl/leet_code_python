

def solution(root):
    if not root:
        return 0
    return 1 + solution(root.left) + solution(root.right)


def solution_2(root):
    if not root: return 0
    left_height = 0
    left_node = root
    right_height = 0
    right_node = root
    while left_node:
        left_node = left_node.left
        left_height += 1
    while right_node:
        right_node = right_node.right
        right_height += 1
    if left_height == right_height:
        return pow(2, left_height) - 1
    return 1 + solution_2(root.left) + solution_2(root.right)



