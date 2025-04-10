import java.util.*;
class Solution {
    public int[] solution(int[] array, int[][] commands) {
        
        int[] answer = new int[commands.length];
        int k = 0;
        for(int i = 0; i < commands.length; i++) {
            int[] array1 = Arrays.copyOfRange(array, commands[i][0]-1, commands[i][1]);
            Arrays.sort(array1);
            answer[i] = array1[commands[i][2] - 1];
            
        }
        
        return answer;
    }
}