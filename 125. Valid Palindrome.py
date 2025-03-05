class Solution:
    def isPalindrome(self, s: str) -> bool:
        converted_s = ''.join([char.lower() for char in s if char.isalnum()])
        left, right = 0, len(converted_s)-1
        while left < right:
            if converted_s[left] != converted_s[right]:
                return False
            left += 1
            right -= 1
        return True
