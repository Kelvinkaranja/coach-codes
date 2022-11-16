def rearrangeCharacters(s, target):
    """
        :type s: str
        :type target: str
        :rtype: int
    """
    checker = []
    for e in range(len(target)):
            perms = abs(s.count(target[e])/target.count(target[e]))
            checker.append(perms)
    return min(checker)
