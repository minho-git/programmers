class Solution {
    public int solution(int n) {
    
        int sum = 0;
        
        for (int i = 2; i <= n; i+=2){
            if(i % 2 == 0) {
                sum += i;
            }
        } 
        
        return sum;
        
        }
}