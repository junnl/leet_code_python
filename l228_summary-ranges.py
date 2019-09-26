

def solution(nums):
    if not nums: return []
    # 一直动的指针
    i = 0
    n = len(nums)
    res = []
    while i < n:
        # 记录开始的指针
        start = i
        while i < n - 1 and nums[i] + 1 == nums[i + 1]:
            i += 1
        # 相等说明, 只有一个数
        if start == i:
            res.append(str(nums[i]))
        else:
            res.append("{}->{}".format(nums[start], nums[i]))
        i += 1
    return res



