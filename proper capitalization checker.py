def detectCapitalUse(word):
    """
        :type word: str
        :rtype: bool
    """
    #Find all caps
    if word.isupper():
        return True
    #Find all lower
    elif word.islower():
        return True
    #Check if first digit is upper and the rest lower
    elif word[1:].islower():
        return True
    else:
        return False
