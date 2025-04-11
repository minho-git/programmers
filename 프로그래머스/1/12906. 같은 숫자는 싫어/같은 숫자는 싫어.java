import java.util.*;

public class Solution {
    public int[] solution(int []arr) {
//         List<Integer> list = new ArrayList();
        
//        for(int i = 0; i < arr.length; i++) {
//            if(i == 0) {
//                list.add(arr[0]);
//            } else {
//                if(arr[i-1] != arr[i]) {
//                    list.add(arr[i]);
//                }
//            } 
//        }
        
        
//         int[] answer = new int[list.size()];
//         for(int i = 0; i < list.size(); i++) {
//             answer[i] = list.get(i);
//         }
        
//         return answer;
        
        Stack<Integer> stack = new Stack();
        for(Integer num : arr) {
            if(stack.empty()) {
                stack.push(num);
            } else if(stack.peek() != num){
                stack.push(num);
            }
        }
        
        
        int[] answer = new int[stack.size()];
        for(int i = 0; i < stack.size(); i++) {
            answer[i] = stack.get(i);
        }
        
        return answer;
    }
}