def countAndSay(n):
    """
    :type n: int
    :rtype: str
    """
    #number = {1:'one',2:'two',3:'three',4:'four',5:'five',}
    #count = 0
    #k = str(n)
    #res = []
    #for i in range(0,len(k)):
    #    currcount = 0
    #    for j in range(i,len(k)):
     
        
    if n == 1:
        return '1'
    x = '1'
    while n > 1:
        # each round, read itself
        x = self.count(x)
        n -= 1
    return x

def count(self, x):
    m = list(x)
    res = []
    m.append(None)
    i , j = 0 , 0
    while i < len(m) - 1:
        j += 1
        if m[j] != m[i]:
            # note j - i is the count of m[i]
            res += [j - i, m[i]]
            i = j
    return ''.join(str(s) for s in res)