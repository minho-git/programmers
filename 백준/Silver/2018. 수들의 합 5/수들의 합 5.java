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

        int[] array = new int[N];

        for (int i = 0; i < N; i++) {
            array[i] = i + 1;
        }

        int sum = 0, lt = 0, answer = 0;

        for (int rt = 0; rt < N; rt++) {

            sum += array[rt];
            if (sum == N) {

                sum -= array[lt];
                lt++;
                answer++;
            } else if (sum > N) {
                while (sum > N) {

                    sum -= array[lt];
                    lt++;

                    if (sum == N) {
                        answer++;
                        sum -= array[lt];
                        lt++;
                    }
                }
            }


        }

        System.out.println(answer);

    }
}
