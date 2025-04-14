class Solution {
    public int[] solution(int n, int m) {
        
        int[] arr = new int[2];
        int mul = n * m;
        
        //최대공약수
        while(m != 0) {
            int temp = m;
            m = n % m;
            n = temp;
            
        }
        
        arr[0] = n;
        
        //최소공배수
        arr[1] = mul / arr[0];
        
        return arr;
    }
}