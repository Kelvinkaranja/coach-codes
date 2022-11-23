'''

A palindrome is a number that is identical looking at it from left to right and also right to left. 
this function also allows for checking of string palindromes.

'''

def isPalindrome(x):
    """
        :type x: int
        :rtype: bool
        """
    #convert to string
    fwd = str(x)
    #reverse the string
    rev = fwd[-1::-1]
    #compare the strings
    return fwd==rev
