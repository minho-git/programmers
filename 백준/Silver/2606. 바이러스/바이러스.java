import java.io.*;
import java.util.*;

public class Main {

    static int N, M;
    static boolean[][] graph;
    static boolean[] visited;
    static int answer;

    private static void dfs(int idx) {
        visited[idx] = true;
        answer++;
        for (int i = 1; i <= N; i++) {
            if (visited[i] == false && graph[idx][i]) {
                dfs(i);
            }
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        N = Integer.parseInt(br.readLine());
        M = Integer.parseInt(br.readLine());

        graph = new boolean[N + 1][N + 1];
        visited = new boolean[N + 1];

        // 1. graph에 연결 정보 채우기
        for (int i = 0; i < M; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());

            graph[x][y] = true;
            graph[y][x] = true;
        }

        // 2. dfs 호출

        dfs(1);

        // 3. 출력
        bw.write(String.valueOf(answer - 1)); // 1도 포함이므로 빼줘야함.

        br.close();
        bw.close();
    }
}
