def largePower(a, b, m):
    # Base Cases
    if (b == 0):
        return 1
    # If b is Even
    if (b % 2 == 0):
        y = largePower(a, b / 2, m)
        return (y * y) % m
    # If b is Odd
    else:
        y = a % m
        return (y * largePower(a, b - 1, m)) % m


print(largePower(14,52,33))