import java.util.*;

class Solution {
    public int solution(int[] sides) {
        
        List<Integer> result = new ArrayList();
        for(int i =0; i < sides.length; i++){
            result.add(sides[i]);
        }
        
        Collections.sort(result);
        
        if(result.get(0) + result.get(1) > result.get(2)) {
            return 1;
            
        } else {
            return 2;
        }
    }
}