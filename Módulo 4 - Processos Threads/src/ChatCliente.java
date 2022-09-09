import java.io.IOException;
import java.io.InputStream;
import java.io.PrintStream;
import java.net.Socket;
import java.net.UnknownHostException;
import java.util.List;
import java.util.Scanner;

public class ChatCliente {
    public static void main(String[] args) {
        Cliente c = new Cliente("127.0.0.1", 12345);
        try {
            c.executa();
        } catch(Exception e) {
            e.printStackTrace();
        }
    }
}

// Classe do cliente e suas dependências
class Cliente {
    private String ip;
    private int porta;
    
    public Cliente(String ip, int porta) {
        this.ip = ip;
        this.porta = porta;
    }

    public void executa() throws UnknownHostException, IOException {
        Socket socket = new Socket(this.ip, this.porta);
        System.out.println("O cliente se conectou");

        // Thread para receber as mensagens do servidor
        Recebedor recebedor = new Recebedor(socket.getInputStream());
        new Thread(recebedor).start();

        // Lê mensagens do teclado e envia para o servidor
        Scanner teclado = new Scanner(System.in);
        PrintStream saida = new PrintStream(socket.getOutputStream());

        while(teclado.hasNextLine()) {
            saida.println(teclado.nextLine());
        }

        // Fechando todos os I/O
        saida.close();
        teclado.close();
        socket.close();
    }

    // Dependência do cliente para manter um canal aberto com o servidor
    class Recebedor implements Runnable {
        private InputStream servidor;
        
        public Recebedor(InputStream servidor) {
            this.servidor = servidor;
        }    
    
        public void run() {
            // Recebe as mensagens do servidor e printa
            Scanner scanner = new Scanner(this.servidor);
    
            while(scanner.hasNextLine()) {
                System.out.println(scanner.nextLine());
            }
        }
    }
}
