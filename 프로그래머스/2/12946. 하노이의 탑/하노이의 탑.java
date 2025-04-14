import java.util.*;

class Solution {
    public int[][] solution(int n) {

        List<String> list = new ArrayList<>();
        move(n, 1, 3,  list);
        System.out.println(list);
        int[][] array = new int[list.size()][2];
        for (int i = 0; i < list.size(); i++) {
            String replaced = list.get(i).replace("[", "").replace("]", "");
            String[] split = replaced.split(",");
            for (int j = 0; j < 2; j++) {
                array[i][j] = Integer.parseInt(split[j]);
            }
        }
        
        return array;
    }
    
    public static void move(int no, int x, int y, List<String> list) {
        if(no > 1) {
            move(no - 1, x, 6 -x -y, list);
        }
        list.add("[" + x + "," + y + "]");

        if(no > 1) {
            move(no - 1, 6 - x - y, y, list);
        }
    }
}