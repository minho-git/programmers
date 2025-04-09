class Solution {
    public String solution(int age) {
        
        int tmp = 0;
        String str = age + "";
        char[] chars = str.toCharArray();
        for(int i = 0; i < chars.length; i++) {
            
            tmp = chars[i] + ('a' - '0');
            chars[i] = (char)tmp;
        }
        
        
        String answer = new String(chars);
        return answer;
    }
}