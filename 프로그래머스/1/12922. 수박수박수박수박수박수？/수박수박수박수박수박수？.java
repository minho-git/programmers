class Solution {
    public String solution(int n) {
        StringBuilder sb = new StringBuilder();
        
        for(int i = 1; i < n+1; i++) {
            if(i % 2 == 0) {
                sb.append("박");
            } else {
                sb.append("수");
            }
        }
        
        String answer = sb.toString();
        return answer;
    }
}