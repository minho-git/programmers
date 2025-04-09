class Solution {
    public int solution(int order) {
        
        int answer = 0;
        String s = order + "";
        String[] array = s.split("");
        for(String num : array) {
            if(num.equals("3") || num.equals("6") || num.equals("9")) {
                answer++;
            }
        }
        
        return answer;
    }
}