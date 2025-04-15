import java.io.*;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {

    static int N, M;
    static boolean[][] graph;
    static boolean[] visited;
    static int answer;

    private static void dfs(int idx) {
        visited[idx] = true;
        for (int i = 1; i <= N; i++) {
            if (visited[i] == false && graph[idx][i]) {
                dfs(i);
            }
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        StringTokenizer st1 = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st1.nextToken());
        M = Integer.parseInt(st1.nextToken());

        graph = new boolean[N + 1][N + 1];
        visited = new boolean[N + 1];

        // 1. graph에 연결 정보 채우기
        for (int i = 0; i < M; i++) {
            StringTokenizer st2 = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(st2.nextToken());
            int y = Integer.parseInt(st2.nextToken());

            graph[x][y] = true;
            graph[y][x] = true;
        }


        // 2. dfs 호출
        for (int i = 1; i < N+1; i++) {
            if (!visited[i]) {
                dfs(i);
                answer++;
            }
            //count 합이 전체 노드 갯수랑 같은 경우
            if (answer == N) {
                break;
            }
        }

        // 3. 출력
        bw.write(String.valueOf(answer)); // 1도 포함이므로 빼줘야함.

        br.close();
        bw.close();
    }
}
