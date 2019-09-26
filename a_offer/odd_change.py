def odd_change(x, y):
    if x > y:
        return False
    if x == y:
        return True

    if x % 2 == 1:
        return odd_change(2 * x, y)
    return odd_change(x + 1, y) or odd_change(2 * x, y)


print(odd_change(3,  6))



