import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    static int T, M, N, K, X, Y, answer;
    static boolean[][] graph;
    static boolean[][] visited;



    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        T = Integer.parseInt(br.readLine());

        for (int i = 0; i < T; i++) {
            answer = 0;
            //입력 받기
            StringTokenizer st = new StringTokenizer(br.readLine());
            M = Integer.parseInt(st.nextToken());
            N = Integer.parseInt(st.nextToken());
            K = Integer.parseInt(st.nextToken());

            graph = new boolean[M+2][N+2];
            visited = new boolean[M+2][N+2];

            for (int j = 0; j < K; j++) {
                st = new StringTokenizer(br.readLine());
                X = Integer.parseInt(st.nextToken()) + 1;
                Y = Integer.parseInt(st.nextToken()) + 1;

                graph[X][Y] = true;
            }


            //dfs(실행)
            for (int k = 1; k <= M; k++) {
                for (int j = 1; j <= N; j++) {
                    if (graph[k][j] && !visited[k][j]) {
                        dfs(k, j);
                        answer++;
                    }

                }
            }
            System.out.println(answer);
        }

        br.close();
    }

    private static void dfs(int i , int j) {
        if (graph[i][j] && !visited[i][j]) {
            visited[i][j] = true;
            dfs(i, j+1);
            dfs(i+1, j);
            dfs(i, j-1);
            dfs(i-1, j);
        }
    }
}