class Solution {
    public String solution(String cipher, int code) {
        
        char[] array = cipher.toCharArray();
        String answer = "";
        
        for(int i = code-1; i < array.length; i+=code) {
            
            answer += array[i];
        } 
        
        
        
        return answer;
    }
}