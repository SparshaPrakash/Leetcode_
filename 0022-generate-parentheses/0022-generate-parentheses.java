import java.util.*;

class Solution {
    public List<String> generateParenthesis(int n) {
        List<String> res = new ArrayList<>();
        backtrack(n, n, new StringBuilder(), res);
        return res;
    }

    private void backtrack(int openLeft, int closeLeft, StringBuilder sb, List<String> res) {
        if (openLeft == 0 && closeLeft == 0) {
            res.add(sb.toString());
            return;
        }
        if (openLeft > 0) {                // you can always place '(' if any are left
            sb.append('(');
            backtrack(openLeft - 1, closeLeft, sb, res);
            sb.setLength(sb.length() - 1); // pop
        }
        if (closeLeft > openLeft) {        // only place ')' if it won't break validity
            sb.append(')');
            backtrack(openLeft, closeLeft - 1, sb, res);
            sb.setLength(sb.length() - 1); // pop
        }
    }
}
