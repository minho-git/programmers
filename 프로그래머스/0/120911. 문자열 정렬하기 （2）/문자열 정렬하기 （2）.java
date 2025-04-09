import java.util.*;
class Solution {
    public String solution(String my_string) {
        String a1 = my_string.toLowerCase();
        char[] a2 = a1.toCharArray();
        Arrays.sort(a2);
        
        String answer = new String(a2);
        return answer;
    }
}