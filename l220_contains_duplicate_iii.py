

def solution(nums, k):
    # 将相同值的索引存储起来
    import collections
    d = collections.defaultdict(list)
    for i, v in enumerate(nums):
        d[v].append(i)

    # 对索引值进行差值的判断, 小于等于k, 则返回True
    for v in d.values():
        for i in range(len(v) - 1):
            if v[i + 1] - v[i] <= k:
                return True

    return False



