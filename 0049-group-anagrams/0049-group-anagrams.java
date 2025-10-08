import java.util.*;

class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> map = new HashMap<>();

        for (String s : strs) {
            int[] freq = new int[26]; // only lowercase 'a'..'z'
            for (int i = 0; i < s.length(); i++) {
                char c = s.charAt(i);
                // if inputs may have uppercase, uncomment next line:
                // c = Character.toLowerCase(c);
                freq[c - 'a']++;
            }

            String key = buildKey(freq); // value-based key from counts
            map.computeIfAbsent(key, k -> new ArrayList<>()).add(s);
        }

        return new ArrayList<>(map.values());
    }

    // Build a compact, collision-free key like "#1#0#0#2...#0"
    private String buildKey(int[] freq) {
        StringBuilder sb = new StringBuilder(26 * 2);
        for (int i = 0; i < 26; i++) {
            sb.append('#').append(freq[i]);
        }
        return sb.toString();
    }
}
