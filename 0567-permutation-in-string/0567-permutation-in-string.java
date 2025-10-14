class Solution {
    public boolean checkInclusion(String s1, String s2) {
        int n1 = s1.length(), n2 = s2.length();
        if (n1 > n2) return false;

        int[] c1 = new int[26];
        int[] c2 = new int[26];

        // seed counts for s1 and the first window in s2
        for (int i = 0; i < n1; i++) {
            c1[s1.charAt(i) - 'a']++;
            c2[s2.charAt(i) - 'a']++;
        }
        if (equals26(c1, c2)) return true;

        // slide the window over s2
        for (int i = n1; i < n2; i++) {
            c2[s2.charAt(i) - 'a']++;           // add new right char
            c2[s2.charAt(i - n1) - 'a']--;      // remove leftmost char
            if (equals26(c1, c2)) return true;
        }
        return false;
    }

    private boolean equals26(int[] a, int[] b) {
        for (int i = 0; i < 26; i++) {
            if (a[i] != b[i]) return false;
        }
        return true;
    }
}
