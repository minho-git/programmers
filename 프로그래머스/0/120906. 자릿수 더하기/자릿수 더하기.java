import java.util.*;

class Solution {
    public int solution(int n) {
        
        String result = n + "";
        int answer = 0;
        
        for(int i = 0; i < result.length(); i++) {
            answer += result.charAt(i) - '0';
        }
        
        return answer;
    }
}