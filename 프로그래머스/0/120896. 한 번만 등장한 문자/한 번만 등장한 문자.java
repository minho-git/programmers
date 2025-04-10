import java.util.*;
class Solution {
    public String solution(String s) {
        String answer = "";
        HashMap<Character, Integer> map = new HashMap();
        for(int i = 0; i < s.length(); i++) {
            map.put(s.charAt(i), map.getOrDefault(s.charAt(i), 0) + 1);
        }
        
        for(int i = 0; i < s.length(); i++) {
            if(map.get(s.charAt(i)) == 1) {
                answer += s.charAt(i);
            }
        }
        
        char[] array = answer.toCharArray();
        Arrays.sort(array);
        answer = new String(array);

        return answer;
    }
}