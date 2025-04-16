import java.io.*;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.StringTokenizer;

public class Main {
    static int N, M, R;
    static ArrayList<Integer>[] graph;
    static boolean[] visited;
    static int[] array;
    static int order;

    public static void main(String[] args) throws IOException {

        //입력받기
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        R = Integer.parseInt(st.nextToken());

        graph = new ArrayList[N + 1];
        for (int i = 0; i <= N; i++) {
            graph[i] = new ArrayList<>();
        }
        visited = new boolean[N + 1];
        array = new int[N + 1];

        //그래프 정보 채우기
        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int u = Integer.parseInt(st.nextToken()); //nextToken은 String타입 반환
            int v = Integer.parseInt(st.nextToken());

            graph[u].add(v);
            graph[v].add(u);

        }

        for (int i = 0; i <= N; i++) {
            Collections.sort(graph[i]);
        }

        //dfs 실행
        dfs(R);

        //출력

        for (int i = 1; i <= N; i++) {
            bw.write(String.valueOf(array[i]));
            bw.newLine();
        }

        br.close();
        bw.close();
    }

    private static void dfs(int idx) {
        visited[idx] = true;
        array[idx] = ++order;

        for (int x : graph[idx]) {
            if (visited[x] == false) {
                dfs(x);
            }
        }
    }
}
