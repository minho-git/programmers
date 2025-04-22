import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    static int N;
    static int[][] graph;
    static String answer;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());

        graph = new int[1000][1000];

        for (int i = 1; i <= N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int j = 1; j <= N; j++) {
                int x = Integer.parseInt(st.nextToken());
                graph[i][j] = x;
            }
        }

        graph[N][N] = -1;

        answer = "Hing";
        dfs(1, 1);

        System.out.println(answer);
        
        br.close();
    }

    private static void dfs(int y, int x) {
        if (graph[y][x] == -1) {
            answer = "HaruHaru";
            return;

        }

        int newY = y + graph[y][x];
        int newX = x + graph[y][x];

        if (graph[newY][x] != 0) {
            dfs(newY, x);
        }

        if (graph[y][newX] != 0) {
            dfs(y, newX);

        }
    }
}
