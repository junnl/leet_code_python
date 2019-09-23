

def shortest_palindrome_1(s):  # 暴力法
    r = s[::-1]
    for i in range(len(s) + 1):
        if s.startswith(r[i:]):
            return r[:i] + s


def shortest_palindrome_2(s): # 从前往后递归查找
    j = 0
    # 找到从头开始，最长的回文子串
    for i in range(len(s) - 1, -1, -1):
        if s[i] == s[j]:
            j += 1

    if j == len(s):
        return s
    # 后缀
    suffix = s[j:]
    return suffix[::-1] + shortest_palindrome_2(s[0:j]) + suffix



