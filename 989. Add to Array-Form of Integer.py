import sys
sys.set_int_max_str_digits(10000)

class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        joined_num = int("".join(map(str,num)))

        sum = joined_num + k
        num = []

        while sum > 0:
            num.append(sum%10)
            sum//=10
        num.reverse()
        return (num)
