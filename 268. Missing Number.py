class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = int("".join(map(str,digits)))

        num = num+1
        digits = []

        while num >0:
            digits.append(num%10)
            num//=10

        digits.reverse()
        return digits
