import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);
        int n  = scanner.nextInt();
        if (n == 1) {
            System.out.println(1);
        } else {
            LinkedList<Integer> queue = new LinkedList<>();

            for (int i = 1; i <= n; i++) {
                queue.add(i);
            }

            while (true) {
                queue.remove();
                queue.add(queue.remove());
                if (queue.size() == 1) {
                    break;
                }
            }

            System.out.println(queue.get(0));
        }

    }
}
