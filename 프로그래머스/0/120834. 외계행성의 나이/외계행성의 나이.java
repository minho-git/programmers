class Solution {
    public String solution(int age) {
    
        String str = age + "";
        StringBuilder sb = new StringBuilder();
        
        for(int i = 0; i < str.length(); i++) {
            sb.append((char)(str.charAt(i) + ('a' - '0')));
        }
        
        String answer = sb.toString();
//         char[] chars = str.toCharArray();
//         for(int i = 0; i < chars.length; i++) {
            
//             chars[i] = (char)(chars[i] + ('a' - '0'));
//         }
        
        
//         String answer = new String(chars);
         return answer;
    }
}