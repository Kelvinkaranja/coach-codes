def isIsomorphic(s: str, t: str) -> bool:
    #Declare variables
    d, n = {}, len(s)
    #iterate through string
    for i in range(n):
        #Isolate edge case
        if s[i] in d and d[s[i]] != t[i]:
            return False
        #Add to dictionary
        d[s[i]] = t[i]
    #find unique figures
    s1 = set(list(s))
    s2 = set(list(t))
    if len(s1) != len(s2):
            return False
    return True
