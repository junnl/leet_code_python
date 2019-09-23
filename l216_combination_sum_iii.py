

def solution(k, n):

    def helper(k, start, n, tmp):
        if k == 0:
            if n == 0 :
                res.append(tmp)
            return

        for i in range(start, 10):
            if n - i < 0:
                break
            helper(k - 1, i + 1, n - i, tmp + [i])

    res = []
    helper(k, 1, n, [])
    return res


