import java.util.*;

class Solution {
    public String solution(String s) {
        
        char[] c = s.toCharArray();
        Arrays.sort(c);
        
        String answer = (new StringBuilder(new String(c)).reverse().toString());
        
//         List<Character> list = new ArrayList();
//         for(int i = 0; i < c.length; i++) {
//             list.add(c[i]);
//         }
//         Collections.sort(list);
//         Collections.reverse(list);

        
//         String answer = "";
//         for(Character cc : list) {
//             answer += cc;
//         }

        
        // char tmp = ' ';
        // for(int i = 0; i < c.length - 1; i++) {
        //     for(int j = i + 1; j < c.length; j++) {
        //         if(c[i] < c[j]) {
        //             tmp = c[i];
        //             c[i] = c[j];
        //             c[j] = tmp;
        //         }
        //     }
        // }
        
        // String answer = String.valueOf(c);
        
        return answer;
    }
}