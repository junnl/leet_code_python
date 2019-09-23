

def longest_substring_without_repeating_characters(s):
    max_s = 0
    start = 0
    for i in range(len(s)):
        while (s[i] in s[start:i]):
            start += 1
        max_s = (i - start + 1) if (i - start + 1) >= max_s else max_s
    return max_s


if __name__ == '__main__':
    ret = longest_substring_without_repeating_characters('abcabcbb')
    print(ret)

