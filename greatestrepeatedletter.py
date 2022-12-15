def greatestLetter(self, s):
        '''
        Given a string of English letters s, return the greatest English letter which occurs as both a lowercase and uppercase letter in s. 
        The returned letter should be in uppercase. If no such letter exists, return an empty string.

        An English letter b is greater than another letter a if b appears after a in the English alphabet.
        '''
        """
        :type s: str
        :rtype: str
        """
        #Create an empty list
        output=['']
        #Iterate through the string
        for i in range(len(s)):
            if s[i].isupper() and s[i].lower() in s:
                output.append(s[i])
        output.sort()
        return output[-1]
