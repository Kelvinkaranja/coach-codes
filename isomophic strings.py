def isIsomorphic(s: str, t: str) -> bool:
    d, n = {}, len(s)
    for i in range(n):
        if s[i] in d and d[s[i]] != t[i]:
            return False
        d[s[i]] = t[i]
    s1 = set(list(s))
    s2 = set(list(t))
    if len(s1) != len(s2):
            return False
    return True