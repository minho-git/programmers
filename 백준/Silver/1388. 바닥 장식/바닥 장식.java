import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {

    static int N, M, count;
    static String[][] graph;
    static boolean[][] visited;


    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        graph = new String[N + 2][M + 2];
        visited = new boolean[N + 2][M + 2];

        for (int i = 1; i <= N; i++) {
            String str = br.readLine();
            for (int j = 1; j <= M; j++) {
                graph[i][j] = String.valueOf(str.charAt(j - 1));
            }
        }

        for (int i = 1; i <= N; i++) {
            for (int j = 1; j <= M; j++) {
                if (graph[i][j] != null && !visited[i][j]) {
                    dfs(i, j);
                    count++;
                }
            }
        }


        System.out.println(count);

        br.close();
    }

    private static void dfs(int y, int x) {

        visited[y][x] = true;
        if (graph[y][x].equals("-")) {
            if (graph[y][x + 1] == null) {
                return;
            }
            if (graph[y][x + 1].equals("-")) {
                dfs(y, x + 1);
            }
        } else if (graph[y][x].equals("|")) {
            if (graph[y+1][x] == null) {
                return;
            }
            if (graph[y+1][x].equals("|")) {
                dfs(y+1, x);
            }
        }
    }
}
