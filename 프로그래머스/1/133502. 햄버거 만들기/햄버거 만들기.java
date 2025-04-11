import java.util.*;
class Solution {
    public int solution(int[] ingredient) {
        int answer = 0;
        int last = 0;
        Stack<Integer> stack = new Stack();
        
        for(int i = 0; i < ingredient.length; i++) {
            stack.push(ingredient[i]);
            last++;
            if(stack.size() >= 4 && stack.get(last-1) == 1 && stack.get(last-2) == 3 
               &&  stack.get(last-3) == 2 && stack.get(last-4) == 1) {
                stack.pop();
                stack.pop();
                stack.pop();
                stack.pop();
                last = last - 4;
                answer++;
                    
            } 
        }

        return answer;
    }
}