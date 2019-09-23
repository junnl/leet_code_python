

def house_robber(nums):
    prev = 0
    cur = 0
    for x in nums:
        temp = cur
        cur = max(prev + x, cur)
        prev = temp
    return cur

