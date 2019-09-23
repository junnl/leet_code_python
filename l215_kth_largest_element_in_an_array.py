import heapq


def find_kth_largest(nums, k) -> int:
    return heapq.nlargest(k, nums)[-1]


