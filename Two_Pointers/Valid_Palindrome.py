class Solution:
    def isPalindrome(self, s: str) -> bool:

        newstring = ''

        for c in s:
            if ord(c) >= ord('a') and ord(c) <= ord('z') or ord(c) >= ord('A') and ord(c) <= ord('Z') or ord(c) >= ord('0') and ord(c) <= ord('9'):
                newstring = newstring + c.lower()

        for i in range(0, len(newstring)):
            if newstring[i] != newstring[-1 -i]:
                return False

        return True

class Solution:
    def isPalindrome(self, s: str) -> bool:
        list = []
        for c in s:
            if c.isalnum() == True:
                list.append(c.lower())
        s = "".join(list)

        left = 0
        right = len(s) - 1
        while left < right:
            if s[left] == s[right]:
                left +=1
                right -=1
            else:
                return False
        return True