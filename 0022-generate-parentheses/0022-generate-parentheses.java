import java.util.*;

class Solution {
    public List<String> generateParenthesis(int n) {
        List<String> res = new ArrayList<>();
        dfs(n, n, "", res);
        return res;
    }

    private void dfs(int openLeft, int closeLeft, String cur, List<String> res) {
        if (openLeft == 0 && closeLeft == 0) {
            res.add(cur);
            return;
        }
        if (openLeft > 0) {
            dfs(openLeft - 1, closeLeft, cur + "(", res);
        }
        if (closeLeft > openLeft) {
            dfs(openLeft, closeLeft - 1, cur + ")", res);
        }
    }
}
