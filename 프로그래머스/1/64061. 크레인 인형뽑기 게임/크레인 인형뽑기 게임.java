import java.util.*;

class Solution {
    public int solution(int[][] graph, int[] moves) {
        int N = graph.length;

        ArrayList<Stack<Integer>> list = new ArrayList<>();
        for (int i = 0; i < N; i++) {
            list.add(new Stack<>());
        }

        // 각 열을 스택으로 변환 (아래 → 위 순서로 쌓기)
        for (int i = 0; i < N; i++) {
            for (int j = N - 1; j >= 0; j--) {
                if (graph[j][i] != 0) {
                    list.get(i).push(graph[j][i]);
                }
            }
        }

        Stack<Integer> stack = new Stack<>();
        int count = 0;

        for (int i = 0; i < moves.length; i++) {
            int num = moves[i];
            Stack<Integer> col = list.get(num - 1);
            if (!col.isEmpty()) {
                int doll = col.pop();  // 딱 한 번만 꺼냄
                if (!stack.isEmpty() && stack.peek() == doll) {
                    stack.pop();
                    count += 2;
                } else {
                    stack.push(doll);
                }
            }
        }

        return count;
    }
}
