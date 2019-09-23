

def two_sum(nums, target):
    d = {}
    for i, j in enumerate(nums):
        if d.get(target - j) is not None:
            return sorted([i, d.get(target - j)])
        d.update({j: i})


if __name__ == '__main__':
    print(two_sum([2, 7, 11, 15], 9))


