import java.util.*;

class Solution {
    public int solution(int[] numbers) {
        
        Arrays.sort(numbers);
        int len = numbers.length;
        int max = Math.max(numbers[0] * numbers[1], numbers[len - 1] * numbers[len - 2]);
        
        return max;
    }
}