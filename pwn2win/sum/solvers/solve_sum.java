import javax.net.SocketFactory;
import javax.net.ssl.SSLSocketFactory;
import java.io.IOException;
import java.io.PrintStream;
import java.net.Socket;
import java.util.InputMismatchException;
import java.util.Scanner;

public class solve_sum {
    public static void main(String[] args) throws IOException {
        SocketFactory factory = SSLSocketFactory.getDefault();
        Socket socket = factory.createSocket("programming.pwn2.win", 9000);
        Scanner ins = new Scanner(socket.getInputStream());
        PrintStream ps = new PrintStream(socket.getOutputStream());
        int sum = 0;
        while (true) {
            try {
                final int a = ins.nextInt();
                if (a == 0) {
                    ps.print(String.format("%d\n", sum));
                    ps.flush();
                    System.out.println(String.format("sent: %d", sum)); // for debugging purposes
                    sum = 0;
                }
                else {
                    sum += a;
                }
            }
            catch (InputMismatchException e) {
                // if unable to read a numeric value, then it's the flag
                System.out.println("flag: " + ins.nextLine());
                break;
            }
        }
    }
}

