def isPalindrome(x):
    """
    :type x: int
    :rtype: bool
    """
    if x < 0:
        return False
    temp, res = x, 0
    while x > 0:
        res = (res * 10) + x % 10
        x = x/10
    if res == temp:
        return True
    else:
        return False