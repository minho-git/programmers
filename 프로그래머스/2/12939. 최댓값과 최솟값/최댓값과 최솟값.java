import java.util.*;

class Solution {
    public String solution(String s) {
        String[] str = s.split(" ");
        
        int[] num = new int[str.length];
        for(int i = 0; i < str.length; i++) {
            if(str[i].contains("-")) {
                str[i] = str[i].replace("-", "");
                num[i] =  -Integer.parseInt(str[i]);
            } else {
                num[i] =  Integer.parseInt(str[i]);
            }
            
        }
        
        
        Arrays.sort(num);
        
        String answer = num[0] + " " + num[num.length-1];
        return answer;
    }
}