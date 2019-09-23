

def get_kth(nums1, start1, end1, nums2, start2, end2, k):
    len1 = end1 - start1 + 1
    len2 = end2 - start2 + 1
    if len1 > len2:
        return get_kth(nums2, start2, end2, nums1, start1, end1, k)

    if len1 == 0:
        return nums2[start2 + k - 1]

    if k == 1:
        return min(nums1[start1], nums2[start2])

    i = start1 + min(len1, k // 2) - 1
    j = start2 + min(len2, k // 2) - 1

    if nums1[i] > nums2[j]:
        return get_kth(nums1, start1, end1, nums2, j + 1, end2, k - (j - start2 + 1))
    return get_kth(nums1, i + 1, end1, nums2, start2, end2, k - (i - start1 + 1))


def median_of_two_sorted_arrays(nums1, nums2):
    # 求k小数法
    left = (len(nums1) + len(nums2) + 1) // 2
    right = (len(nums1) + len(nums2) + 2) // 2
    return (
        get_kth(nums1, 0, len(nums1) - 1, nums2, 0, len(nums2) - 1, left) +
        get_kth(nums1, 0, len(nums1) - 1, nums2, 0, len(nums2) - 1, right)
    ) / 2


if __name__ == '__main__':
    print(median_of_two_sorted_arrays([1,2,4], [3,4,5]))