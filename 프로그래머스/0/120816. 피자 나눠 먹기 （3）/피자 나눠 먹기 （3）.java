class Solution {
    public int solution(int slice, int n) {
        int i = 1;
        while(true) {
            if(((i * slice) / n) >= 1) {
                break;
            }
            i++;
        }
        return i;
    }
}