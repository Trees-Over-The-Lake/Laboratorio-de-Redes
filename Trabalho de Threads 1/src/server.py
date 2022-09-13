import socket
import threading

class Server:
    HOST: str 
    PORT: str # Porta do serviço
    
    conexao: socket.socket # Conexão que será aberta

    # Construtor para criar um servidor
    def __init__(self, host: str, port: int) -> None:
        self.HOST = host
        self.PORT = port

    # Abrindo o servidor tanto para IPv4 quanto para IPv6
    def open(self) -> None:
        addr = (self.HOST, self.PORT)  # Rodando em todas as interfaces de rede
        
        if socket.has_dualstack_ipv6():
            self.conexao = socket.create_server(addr, family=socket.AF_INET6, dualstack_ipv6=True)
            print(f"Servidor aberto: {self.HOST}:{self.PORT}, usando dual-stacking IPv4 e IPv6!")
            
        else:
            self.conexao = socket.create_server(addr)
            print(f"Servidor aberto: {self.HOST}:{self.PORT}!")

    # Administrando as conexões
    def handle(self):
        cliente, endereco = self.conexao.accept()
        
        print(f"Cliente {cliente} conectado: {endereco[0]}:{endereco[1]}")

def main() -> None:
    # Abrindo o servidor em todos os dispositivos de rede 
    server = Server('::', 25665)
    server.open()
    
    while True:
        cliente, endereco = server.conexao.accept()
        
        print(f"{cliente} {endereco[0]}:{endereco[1]}")


if __name__ == '__main__':
    main()