import java.io.*;
import java.lang.reflect.Array;
import java.util.ArrayList;
import java.util.Collection;
import java.util.Collections;
import java.util.StringTokenizer;

public class Main {

    static int N, M, V;
    static ArrayList<Integer>[] graph;
    static boolean[] visited;
    static ArrayList<Integer> queue;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        V = Integer.parseInt(st.nextToken());

        visited = new boolean[N + 1];
        queue = new ArrayList<>();
        graph = new ArrayList[N+1];
        for (int j = 0; j <= N; j++) {
            graph[j] = new ArrayList<>();
        }

        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());

            graph[x].add(y);
            graph[y].add(x);
        }

        for (int i = 1; i <= N; i++) {

            Collections.sort(graph[i]);
        }

        dfs(V);
        System.out.println();

        visited = new boolean[N + 1];
        bfs();

        br.close();

    }

    private static void dfs(int idx) {
        visited[idx] = true;
        System.out.print(idx + " ");

        for (int i =0; i < graph[idx].size(); i++) {
            if (visited[graph[idx].get(i)] == false) {
                dfs(graph[idx].get(i));
            }
        }

    }

    private static void bfs() {
        queue.add(V);
        visited[V] = true;

        while (!queue.isEmpty()) {
            Integer idx = queue.remove(0);
            System.out.print(idx + " "); //idx= 1

            for (int i = 0; i < graph[idx].size(); i++) {
                if (visited[graph[idx].get(i)] == false) {
                    queue.add(graph[idx].get(i));
                    visited[graph[idx].get(i)] = true;

                }
            }
        }


    }

}