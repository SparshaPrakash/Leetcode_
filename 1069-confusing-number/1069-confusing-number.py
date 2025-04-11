class Solution:
    def confusingNumber(self, n: int) -> bool:
        non_rotate = {2,3,4,5,7}
        rotate = {0:0, 1:1,6:9, 8:8, 9:6}
        new_num = 0

        num = n

        while num:
            digit = num % 10
            if digit in non_rotate:
                return False
            new_num = new_num * 10 + rotate[digit]
            num //= 10

        return True if new_num != n else False
        