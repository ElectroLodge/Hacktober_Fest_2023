import java.io.BufferedInputStream;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.ServerSocket;
import java.net.Socket;
import java.nio.channels.ServerSocketChannel;

public class Server1 {
    public static void main(String[] args) throws Exception{
        ServerSocket ss = new ServerSocket(4999);
        Socket s = ss.accept();

        System.out.println("client connected...!");

        InputStreamReader in = new InputStreamReader(s.getInputStream());
        BufferedReader bf = new BufferedReader(in);

        String str = bf.readLine();
        System.out.println("Client : "+str);

        PrintWriter pr = new PrintWriter(s.getOutputStream());
        pr.println("yes...");
        pr.flush();
    }
}