import java.util.*;
class Solution {
    boolean solution(String s) {
        boolean answer = true;

        String[] array = s.split("");
        
        HashMap<String, Integer> map = new HashMap();
        
        for(String ss : array) {
            if(ss.equals("p") || ss.equals("P")) {
                map.put("p", map.getOrDefault("p", 0) + 1);
            } else if (ss.equals("y") || ss.equals("Y")) {
                map.put("y", map.getOrDefault("y", 0) + 1);
            }
        }
        
        if(!(map.get("p") == map.get("y"))) {
            answer = false;
        }

        return answer;
    }
}