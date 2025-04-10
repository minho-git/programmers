import java.util.*;
class Solution {
    public String solution(String[] participant, String[] completion) {
        
        String answer = "";
        HashMap<String, Integer> map1 = new HashMap();
        for(String s : participant) {
            map1.put(s, map1.getOrDefault(s, 0) + 1);
        }
        
        HashMap<String, Integer> map2 = new HashMap();
        for(String s : completion) {
            map2.put(s, map2.getOrDefault(s, 0) + 1);
        }
        
        for(String s : participant) {
            if(!map2.containsKey(s)) {
                answer = s;
            } else if(map1.get(s) > map2.get(s)) {
                answer = s;
            }
        }
        
        return answer;
    }
}