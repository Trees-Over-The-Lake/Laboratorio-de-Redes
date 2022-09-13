package example;
import java.io.IOException;
import java.io.InputStream;
import java.io.PrintStream;
import java.net.ServerSocket;
import java.net.Socket;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class ChatServidor {
    public static void main(String[] args) {
        Servidor s = new Servidor(12345);
        try {
            s.executa();
        } catch(Exception e) {
            e.printStackTrace();
        }
    }
}

// Classe do servidor e suas dependências
class Servidor {
    private int porta;
    private List<PrintStream> clientes;

    public Servidor(int porta) {
        this.porta = porta;
        this.clientes = new ArrayList<PrintStream>();
    }

    public void executa() throws IOException {
        ServerSocket servidor = new ServerSocket(this.porta);
        System.out.println("Servidor aberto na porta: " + this.porta);

        while(true) {
            // Aceitar novos clientes
            Socket cliente = servidor.accept();
            System.out.println("Nova conexão realizada: " + cliente.getInetAddress().getHostAddress());
        
            // Adicionar saida do cliente à lista
            PrintStream ps = new PrintStream(cliente.getOutputStream());
            this.clientes.add(ps);

            // Cria um tratador de clientes em uma nova thread
            TrataCliente tc = new TrataCliente(cliente.getInputStream(), this);
            new Thread(tc).start();
        }
    }

    public void distribuiMensagem(String msg) {
        // Broadcast da mensagem
        for(PrintStream cliente : this.clientes) {
            cliente.println(msg);
        }
    }

    // Dependência do servidor
    // Controla os clientes em outra thread
    class TrataCliente implements Runnable {
        private InputStream cliente;
        private Servidor servidor;

        public TrataCliente(InputStream cliente, Servidor servidor) {
            this.cliente = cliente;
            this.servidor = servidor;
        }

        public void run() {
            // Quando chegar uma mensagem distribuir para todos
            Scanner scanner = new Scanner(this.cliente);

            while(scanner.hasNextLine()) {
                servidor.distribuiMensagem(scanner.nextLine());
            }
            
            // Se não houver mais mensagens, então feche o scanner
            scanner.close();
        }
    }
}