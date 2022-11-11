def isIsomorphic(s: str, t: str) -> bool:
    #Assign variables
    d, n = {}, len(s)
    #Iterate through the string
    for i in range(n):
        #Check for conflicting letters
        if s[i] in d and d[s[i]] != t[i]:
            return False
        #Add to dictionary d
        d[s[i]] = t[i]
    #Create 2 sets for each string for comparison
    s1 = set(list(s))
    s2 = set(list(t))
    if len(s1) != len(s2):
            return False
    return True
