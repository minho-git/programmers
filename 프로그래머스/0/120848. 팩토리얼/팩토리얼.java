class Solution {
    public int solution(int n) {
        
        int x = 1;
        int fact = 1; 
        
        //factorial
        while(true) {
            
            fact *= x;
            if(fact > n) {
                return x-1;
            } else if(fact == n) {
                return x;
            }
            x++;
            
        }
        
        
        
    }
    
}