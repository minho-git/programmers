import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.HashMap;
import java.util.StringTokenizer;


public class Main {

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int[] array = new int[9];


        for (int i = 0; i < 9; i++) {
            array[i] = Integer.parseInt(br.readLine());
        }

        Arrays.sort(array);

        for (int i = 0; i < 3; i++) {
            int n1 = array[i];
            for (int j = i + 1; j < 4; j++) {
                int n2 = array[j];
                for (int k = j + 1; k < 5; k++) {
                    int n3 = array[k];
                    for (int q = k + 1; q < 6; q++) {
                        int n4 = array[q];
                        for (int w = q + 1; w < 7; w++) {
                            int n5 = array[w];
                            for (int e = w + 1; e < 8; e++) {
                                int n6 = array[e];
                                for (int r = e + 1; r < 9; r++) {
                                    int n7 = array[r];
                                    if (n1 + n2 + n3 + n4 + n5 + n6 + n7 == 100) {
                                        System.out.println(n1);
                                        System.out.println(n2);
                                        System.out.println(n3);
                                        System.out.println(n4);
                                        System.out.println(n5);
                                        System.out.println(n6);
                                        System.out.println(n7);
                                        return;
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }





    }
}
