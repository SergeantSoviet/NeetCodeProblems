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