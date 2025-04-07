class Solution {
    public double solution(int[] numbers) {
        double sum = 0;
        for(double number : numbers) {
            sum += number;
        }
        
        double avg = sum / numbers.length;
        return avg;
    }
}