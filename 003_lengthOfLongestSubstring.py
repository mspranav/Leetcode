def lengthOfLongestSubstring(s: str) -> int:
    ans,i,j = 0,0,0
    res = []
    while(i<len(s) and j < len(s)):
        if(s[j] not in res):
            res.append(s[j])
            j+=1
            ans = max(ans, j-i)
            
        else:
            res.remove(s[i])
            i+=1
    return ans