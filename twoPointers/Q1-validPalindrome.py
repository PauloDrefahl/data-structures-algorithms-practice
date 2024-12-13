class Solution(object):
    def isPalindrome(self, s):
        s = filter(lambda c : c.isalnum(), s.lower()) #here i used filteer with an anonymous function to keep only letters and numbers in the lower case string 
        if s == s[::-1]: 
            return True
        return False