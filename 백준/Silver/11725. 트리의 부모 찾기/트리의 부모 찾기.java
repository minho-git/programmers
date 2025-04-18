import java.io.*;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Main {

    static int N;
    static ArrayList<Integer>[] graph;
    static boolean[] visited;
    static int[] answer;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine()); //노드 수

        answer = new int[N + 1];
        visited = new boolean[N + 1];
        graph = new ArrayList[N + 1];
        for (int j = 0; j <= N; j++) {
            graph[j] = new ArrayList<>();
        }


        for (int i = 0; i < N - 1; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());

            graph[x].add(y);
            graph[y].add(x);
        }

        dfs(1, 0);

        for (int i = 2; i <= N; i++) {
            System.out.println(answer[i]);
        }
        br.close();
    }

    private static void dfs(int idx, int before) {
        visited[idx] = true;
        answer[idx] = before;

        for (int i = 0; i < graph[idx].size(); i++) {
            if (visited[graph[idx].get(i)] == false) {
                dfs(graph[idx].get(i), idx);
            }
        }
    }

}