def longestPalindrome(s: str) -> str:
    res = ''
    for i in range(len(s)):
        for j in range(len(s),i,-1):
            if s[i:j] == s[i:j][::-1] and len(res) < len(s[i:j]):
                res = s[i:j]
                break
    return res