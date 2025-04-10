class Solution {
    public String[] solution(String my_str, int n) {
        
        int size = 0;
        int j = 0;
        String[] answer;
        
        if(my_str.length() % n == 0) {
            size = my_str.length() / n;
            answer = new String[size];
        
            for(int i = 0; i < my_str.length(); i=i+n) {
                answer[j] = my_str.substring(i, i+n);
                j++;
            }
        } else {
            size = my_str.length() / n + 1;
            answer = new String[size];
        
            for(int i = 0; i < my_str.length() - n; i=i+n) {
                answer[j] = my_str.substring(i, i+n);
                j++;
            } 
            answer[j] = my_str.substring(my_str.length() - (my_str.length() % n));
        }
        
        return answer;
    }
}