

class Solution {
    public boolean containsDuplicate(int[] nums) {
        HashSet<Integer> values = new HashSet<>();

        for (int n : nums) {
            if (values.contains(n)) {
                return true; // duplicate found
            }
            values.add(n); // store number in the set
        }

        return false; // no duplicates found
    }
}
