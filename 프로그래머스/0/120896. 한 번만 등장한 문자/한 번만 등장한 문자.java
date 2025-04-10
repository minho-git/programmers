import java.util.*;
class Solution {
    public String solution(String s) {
        
        HashSet<String> set = new HashSet();
        String answer = "";
        
        //set에 담고
        String[] array = s.split("");
        for(String ss : array) {
            set.add(ss);
        }
        
        //비교할 배열을 만들고
        Object[] array2 = set.toArray();
        Arrays.sort(array2);
        // System.out.println(Arrays.toString(array2));
        
        //원래 문자열을 리스트로 만들어서
        
        List<String> list = Arrays.asList(array);
        
        for(Object o : array2) {
            if(Collections.frequency(list, o) == 1) {
                answer += o;
            }
        }
        
        
        
        
//         String answer = "";
//         HashMap<Character, Integer> map = new HashMap();
//         for(int i = 0; i < s.length(); i++) {
//             map.put(s.charAt(i), map.getOrDefault(s.charAt(i), 0) + 1);
//         }
        
//         for(int i = 0; i < s.length(); i++) {
//             if(map.get(s.charAt(i)) == 1) {
//                 answer += s.charAt(i);
//             }
//         }
        
//         char[] array = answer.toCharArray();
//         Arrays.sort(array);
//         answer = new String(array);

         return answer;
    }
}