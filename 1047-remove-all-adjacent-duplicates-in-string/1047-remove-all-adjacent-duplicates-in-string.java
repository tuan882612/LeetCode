class Solution {
    public String removeDuplicates(String s) {
        Stack<Character> stack = new Stack<>();
        StringBuilder res = new StringBuilder();
        
        for (int i = 0; i < s.length(); i++) {
            if (stack.isEmpty() || stack.peek() != s.charAt(i)) {
                stack.push(s.charAt(i));
            } else {
                stack.pop();
            }
        }
        
        for (char i: stack) {
            res.append(i);
        }
        
        return res.toString();
    }
}