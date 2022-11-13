def detectCapitalUse(word):
    """
        :type word: str
        :rtype: bool
    """
    if word.isupper():
        return True
    elif word.islower():
        return True
    elif word[1:].islower():
        return True
    else:
        return False
