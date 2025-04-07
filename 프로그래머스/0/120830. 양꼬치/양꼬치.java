class Solution {
    public int solution(int n, int k) {
        int totalN = n * 12000;
        int service = n / 10;
        int totalK = (k-service) * 2000;
        int total = totalN + totalK;
            
        return total;
    }
}