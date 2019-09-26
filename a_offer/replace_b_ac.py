

def replace_b_ac(s):
    i = 0
    while i <= len(s) - 1:
        if s[i] == 'b':
            s = s[:i] + s[i + 1:]
        elif i < len(s) - 1 and s[i] == 'a' and s[i + 1] == 'c':
            s = s[:i] + s[i + 2:]
        else:
            i += 1
    return s

print(replace_b_ac('acb'))



