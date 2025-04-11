import java.util.*;
class Solution {
    boolean solution(String s) {
        
//         String[] array = s.split("");
//         boolean answer = true;
        
//         Stack<String> stack = new Stack();
//         for(int i = 0; i < array.length; i++) {
//             if(array[i].equals("(")) {
//                 stack.push("(");
//             } else if(array[i].equals(")")) {
//                 if(stack.size() == 0) {
//                     return false;
//                 } else {
//                     if(stack.peek().equals("(")) {
//                         stack.pop();
//                     }
//                 }

//             }
//         }
        
//         if(!stack.empty()) {
//             answer = false;
//         }
        
        
//         return answer;
                // Stack에 (이면 넣고, (가 아니면 빼자.!
        // 올바른 괄호만 있다면 stack에는 아무것도 남지 않을 것.
        Stack<Character> stack = new Stack<>();

        for (int i = 0; i < s.length(); i++) {
            char current = s.charAt(i);

            // 여는 괄호 '(' 일 경우 스택에 추가
            if (current == '(') {
                stack.push(current);
            } else {
                // 닫는 괄호 ')' 일 경우 스택에서 여는 괄호 '('를 제거
                if (stack.isEmpty()) {
                    // 스택이 비어있다면 올바르지 않은 괄호
                    return false;
                } else {
                    stack.pop();
                }
            }
        }

        return stack.isEmpty();
    }
}