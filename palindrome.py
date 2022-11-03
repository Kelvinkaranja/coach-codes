'''

A palindrome is a number that is identical looking at it from left to right and also right to left. 
this function also allows for checking of string palindromes.

'''

def isPalindrome(x):
    """
        :type x: int
        :rtype: bool
        """
    fwd = str(x)
    rev = fwd[-1::-1]
    if fwd == rev:
        return True
    else:
        return False
