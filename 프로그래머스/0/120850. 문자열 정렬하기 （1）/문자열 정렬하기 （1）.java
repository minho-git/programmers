import java.util.*;
class Solution {
    public int[] solution(String my_string) {
        
        char[] numbers = my_string.toCharArray();
        List<Integer> list = new ArrayList();
        
        for(int i = 0; i < numbers.length; i++) {
            // if(Character.isDigit(numbers[i])) {
            //     list.add(Character.getNumericValue(numbers[i]));
            // }
            if(numbers[i] >= '0' && numbers[i] <= '9') {
                list.add(numbers[i] - '0');
            }
        }
        Collections.sort(list);
        int[] answer = new int[list.size()];
        for(int i = 0; i < list.size(); i++) {
            answer[i] = list.get(i);
        }
        
        return answer;
    }
}