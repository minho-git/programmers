class Solution {
    public int solution(int num, int k) {
        String num1 = num + "";
        String k1 = k + "";
        
        if(!num1.contains(k1)) {
            return -1;
        }
        
        int answer = num1.indexOf(k1) + 1;
        return answer;
    }
}