import java.io.*;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Main {

    static int N, start, end, z, answer;
    static ArrayList<Integer>[] graph;
    static boolean[] visited;
    static ArrayList<Integer> queue;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine()); //사람 수

        StringTokenizer st = new StringTokenizer(br.readLine());
        start = Integer.parseInt(st.nextToken()); //사람 1
        end = Integer.parseInt(st.nextToken()); // 사람 2

        z = Integer.parseInt(br.readLine()); // 관계 수

        visited = new boolean[N + 1];
        graph = new ArrayList[N + 1];
        for (int j = 0; j <= N; j++) {
            graph[j] = new ArrayList<>();
        }

        for (int i = 0; i < z; i++) {
            st = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());

            graph[x].add(y);
            graph[y].add(x);
        }

        answer = -1;
        dfs(start, 0);
        System.out.println(answer);
        br.close();
    }

    private static void dfs(int idx, int count) {
        visited[idx] = true;

        if (idx == end) {
            answer = count;
            return;
        }

        for (int i = 0; i < graph[idx].size(); i++) {
            if (visited[graph[idx].get(i)] == false) {
                dfs(graph[idx].get(i), count + 1);
            }
        }
    }

}