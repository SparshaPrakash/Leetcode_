class Solution:
    def intToRoman(self, num: int) -> str:
        symList = [["I", 1], ["IV", 4], ["V", 5], ["IX", 9], ["X", 10], ["XL", 40], ["L", 50], ["XC", 90], ["C", 100], ["CD", 400],["D", 500],["CM", 900],["M", 1000]]

        res = ""

        for sym, val in reversed(symList):  # we need to itertate from the bigger value t the smalle rone
            if num // val:   # eg : 1400//1000 -> 1 -> we need to add one M
                count = num // val
                res += (sym * count)
                num = num % val # 1400 % 1000 -> 400 -> removing the thusands place
        return res
        