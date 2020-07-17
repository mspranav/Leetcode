def reverse(x: int) -> int:
    if x > 0:
        s = str(x)
        s = s[::-1]
        return (int(s) if int(s) in range(-2**31,2**31 - 1) else 0)
    else:
        x = x * -1
        s = str(x)
        s = s[::-1]
        return (-1 * int(s) if int(s) in range(-2**31,2**31 - 1) else 0)
    return 0