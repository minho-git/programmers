import java.util.*;

class Solution {
    public String solution(String my_string, int s, int e) {

        String first = my_string.substring(0, s);
        String last = my_string.substring(e + 1);
        String main = my_string.substring(s, e + 1);
        
        StringBuilder sb = new StringBuilder(main);
        sb.reverse();
        
        String after = sb.toString();
        
        return first + after + last;
    }
}