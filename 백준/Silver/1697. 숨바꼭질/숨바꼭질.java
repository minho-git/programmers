import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
    static Queue<Integer> queue = new LinkedList<>();
    static int E;
    static int[] dirX = {-1, 1, 2};
    static int[] visited;

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int S = Integer.parseInt(st.nextToken());
        E = Integer.parseInt(st.nextToken());
        visited = new int[100001];

        if (S == E) {
            System.out.println(0);

        } else {
            bfs(S);
        }


    }

    public static void bfs(int S) {
        queue.add(S);
        int time = 0;

        while (!queue.isEmpty()) {
            int size = queue.size();
            time++;

            for (int i = 0; i < size; i++) {

                int polled = queue.poll();
                for (int j = 0; j < 3; j++) {
                    int next;
                    if (j == 2) {
                        next = dirX[j] * polled;
                    } else {
                        next = polled + dirX[j];
                    }

                    if (next == E) {
                        System.out.println(time);
                        return;

                    } else {
                        if (next >= 0 && next < 100001 && visited[next] == 0) {
                            queue.add(next);
                            visited[next] = 1;
                        }
                    }
                }
            }

        }
    }
}
