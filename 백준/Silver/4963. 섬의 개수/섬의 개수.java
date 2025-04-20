import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static int w, h, count;
    static boolean[][] graph;
    static boolean[][] visited;
    static int[] dirY = {1, 1, 0, -1, -1, -1, 0, 1};
    static int[] dirX = {0, 1, 1, 1, 0, -1, -1, -1};


    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;


        while (true) {
            //입력받기
            st = new StringTokenizer(br.readLine());
            w = Integer.parseInt(st.nextToken());
            h = Integer.parseInt(st.nextToken());

            if (w == 0 && h == 0) {
                break;
            }

            graph = new boolean[h + 2][w + 2];
            visited = new boolean[h + 2][w + 2];
            count = 0;

            //그래프 채우기
            for (int i = 1; i <= h; i++) {
                st = new StringTokenizer(br.readLine());
                for (int j = 1; j <= w; j++) {
                    int x = Integer.parseInt(st.nextToken());
                    graph[i][j] = (x == 1);
                }
            }

            for (int i = 1; i <= h; i++) {
                for (int j = 1; j <= w; j++) {
                    if (graph[i][j] && visited[i][j] == false) {
                        dfs(i, j);
                        count++;
                    }
                }
            }

            System.out.println(count);


        }

        br.close();
    }

    private static void dfs(int y, int x) {
        visited[y][x] = true;
        for (int i = 0; i < 8; i++) {
            int newY = y + dirY[i];
            int newX = x + dirX[i];

            if (graph[newY][newX] && !visited[newY][newX]) {
                dfs(newY, newX);
            }
        }


    }
}
