import java.util.*;
class Solution {
    public String[] solution(String[] strings, int n) {
        
//         String tmp = "";
//         for(int i = 0; i < strings.length; i++) {
//             for(int j = i + 1; j <strings.length; j++){
//                 if(strings[j].charAt(n) < strings[j-1].charAt(n)) {
//                     tmp = strings[j-1];
//                     strings[j-1] = strings[j];
//                     strings[j] = tmp;
                    
//                 } else if(strings[j].charAt(n) == strings[j-1].charAt(n)) {
//                     if(strings[j-1].compareTo(strings[j]) > 0) {
//                         tmp = strings[j-1];
//                         strings[j-1] = strings[j];
//                         strings[j] = tmp;
//                     }
//                 }
//             }
//         }
        
        for(int i = 0; i < strings.length; i++) {
            strings[i] = strings[i].charAt(n) + strings[i];
        }
        
        Arrays.sort(strings);
        
        for(int i = 0; i < strings.length; i++) {
            strings[i] = strings[i].substring(1);
        }  
        

        return strings;
    }
}