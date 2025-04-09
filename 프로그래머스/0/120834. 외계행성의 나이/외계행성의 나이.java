class Solution {
    public String solution(int age) {
    
        String str = age + "";
        char[] chars = str.toCharArray();
        for(int i = 0; i < chars.length; i++) {
            
            chars[i] = (char)(chars[i] + ('a' - '0'));
        }
        
        
        String answer = new String(chars);
        return answer;
    }
}