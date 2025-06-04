import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {

    static int N, S, answer;
    static int[] check;
    static int[] array;

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        check = new int[N + 1];
        S = Integer.parseInt(st.nextToken());

        array = new int[N+1];
        st = new StringTokenizer(br.readLine());

        for (int i = 1; i <= N; i++) {
            array[i] = Integer.parseInt(st.nextToken());
        }
        answer = 0;
        dfs(1);

        if (S == 0) {
            answer--;
        }
        System.out.println(answer);



    }

    public static void dfs(int L) {

        if (L == N + 1) {
            int sum = 0;
            for (int i = 1; i <= N; i++) {
                if (check[i] == 1) {
                    sum += array[i];
                }
            }

            if (sum == S) {
                answer++;
            }

        } else {
            check[L] = 1;
            dfs(L+1);
            check[L] = 0;
            dfs(L + 1);

        }
    }
}