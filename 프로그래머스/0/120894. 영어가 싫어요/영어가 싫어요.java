import java.util.*;
class Solution {
    public long solution(String numbers) {
        numbers = numbers.replace("zero", "0").replace("one", "1").replace("two", "2").replace("three", "3")
            .replace("four", "4").replace("five", "5").replace("six", "6").replace("seven", "7")
            .replace("eight", "8").replace("nine", "9");
    
        char[] nums = numbers.toCharArray();
        Long answer = 0L;
        Long count = 1L;
        
        for(int i = nums.length-1; i >= 0; i--){
            answer += (nums[i] - '0') * count;
            count *= 10;
            
        }
        
        return answer;  
    }
}