import java.util.*;

class Solution {
    public boolean isValid(String s) {
        Map<Character, Character> pairs = new HashMap<>();
        pairs.put(')', '(');
        pairs.put('}', '{');
        pairs.put(']', '[');

        Deque<Character> stack = new ArrayDeque<>();

        for (char c : s.toCharArray()) {
            if (pairs.containsKey(c)) {                 // closing bracket
                if (!stack.isEmpty() && stack.peek() == pairs.get(c)) {
                    stack.pop();
                } else {
                    return false;
                }
            } else {                                     // opening bracket
                stack.push(c);
            }
        }
        return stack.isEmpty();
    }
}
