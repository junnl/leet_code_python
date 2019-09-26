

def solution(A, B, C, D, E, F, G, H):
    if A > E:
        return solution(E, F, G, H, A, B, C, D)
        # 没有重叠的情况
    if B >= H or D <= F or C <= E:
        return abs(A - C) * abs(B - D) + abs(E - G) * abs(F - H)
        # 重叠情况
        # 下边界
    down = max(A, E)
    # 上
    up = min(C, G)
    # 左
    left = max(B, F)
    # 右
    right = min(D, H)
    return abs(A - C) * abs(B - D) + abs(E - G) * abs(F - H) - abs(up - down) * abs(left - right)
