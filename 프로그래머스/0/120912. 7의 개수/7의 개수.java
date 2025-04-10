class Solution {
    public int solution(int[] array) {
        int answer = 0;
        String s = new String();
        for(int i : array) {
            s += i;
        }
        
        char[] array1 = s.toCharArray();
        for(char c : array1) {
            if(c == '7') {
                answer++;
            }
        }
        

        
        return answer;
    }
}