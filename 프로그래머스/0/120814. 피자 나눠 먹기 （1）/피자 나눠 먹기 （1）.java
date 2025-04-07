class Solution {
    public int solution(int n) {
        int count = n / 7;
        if(n % 7 != 0) {
            count++;
        }
        return count;
    }
}