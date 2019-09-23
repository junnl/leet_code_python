

def min_sub_array_len(n, nums):
    l = len(nums)
    sums = 0
    ans = 1000000
    left = 0
    for k in range(l):
        sums += nums[k]
        while sums >= n:
            ans = min(ans, k - left + 1)
            sums -= nums[left]
            left += 1
    return ans if ans != 1000000 else 0





