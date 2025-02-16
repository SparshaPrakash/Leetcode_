class Solution:
    def numberOfWays(self, s: str) -> int:
        count0, count1 = 0, 0  # Counts of '0's and '1's
        count01, count10 = 0, 0  # Counts of "01" and "10" pairs
        result = 0  # Final count of "010" and "101" triplets

        for c in s:
            if c == '0':
                result += count10  # Every "10" before this '0' forms a "101"
                count01 += count1  # Every "1" before this '0' forms a "01" pair
                count0 += 1
            else:  # c == '1'
                result += count01  # Every "01" before this '1' forms a "010"
                count10 += count0  # Every "0" before this '1' forms a "10" pair
                count1 += 1

        return result

            