import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        int[] array = new int[N];
        st = new StringTokenizer(br.readLine());

        for (int i = 0; i < N; i++) {
            array[i] = Integer.parseInt(st.nextToken());
        }

        int lt = 0, sum = 0, answer = 0;

        for (int rt = 0; rt < N; rt++) {
            sum += array[rt];
            if (sum == M) {
                answer++;
                sum -= array[lt];
                lt++;
            }

            while (sum > M) {

                sum -= array[lt++];
                if (sum == M) {
                    answer++;
                    sum -= array[lt];
                    lt++;
                    break;
                }
            }
        }

        System.out.println(answer);
    }
}
