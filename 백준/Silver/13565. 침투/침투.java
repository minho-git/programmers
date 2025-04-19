import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static int M, N;
    static boolean[][] graph;
    static boolean[][] visited;
    static String answer;
    static int[] dirY = {-1, 1, 0, 0};
    static int[] dirX = {0, 0, -1, 1};


    public static void main(String[] args) throws IOException {
        //입력 받기
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        M = Integer.parseInt(st.nextToken());
        N = Integer.parseInt(st.nextToken());

        graph = new boolean[M + 2][N + 2];
        visited = new boolean[M + 2][N + 2];
        answer = "NO";

        // 그래프 채우기
        for (int i = 1; i < M + 1; i++) {
            String str = br.readLine();
            String[] split = str.split("");
            for (int j = 1; j < N + 1; j++) {
                String s = split[j-1];
                if (s.equals("0")) {
                    graph[i][j] = true;
                }
            }
        }

        //dfs
        for (int i = 1; i <= N; i++) {
            if (graph[1][i] && !visited[1][i]) {
                dfs(1, i);
            }
        }

        //출력
        System.out.println(answer);


    }

    private static void dfs(int y, int x) {
        visited[y][x] = true;
        for (int i = 0; i < 4; i++) {
            int newY = y + dirY[i];
            int newX = x + dirX[i];

            if (graph[newY][newX] && !visited[newY][newX]) {
                dfs(newY, newX);
                if (newY == M) {
                    answer = "YES";
                    break;
                }
            }
        }

    }


}