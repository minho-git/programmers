class Solution {
    public String solution(String my_string) {
        
        char[] array = my_string.toCharArray();
        
        for(int i = 0; i < array.length; i++) {
            if(array[i] >= 65 && array[i] <=90) {
                array[i] = (char)(array[i] + 32);
            } else {
                array[i] = (char)(array[i] -  32);
            }
        }

        String answer = new String(array);
        return answer;
    }
}