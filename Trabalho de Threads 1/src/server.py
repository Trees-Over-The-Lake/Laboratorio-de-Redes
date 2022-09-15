import socket
import threading

# Todos os comandos possíveis no servidor
class Commands:  
    def __init__(self, prefixo: str) -> None:
        # Prefixo usado no servidor 
        self.PREFIXO = prefixo
    
    # Comandos usado pelos clientes
    
    # Listar os comandos possíveis
    AJUDA = 'AJUDA'
    # Comprar ingresso
    COMPRAR = 'COMPRAR'
    # Listar ingressos disponíveis
    LISTAR = 'LISTAR'
    # Escolher ingresso
    ESCOLHER = 'ESCOLHER'

    
    # Mensagens de resposta para o usuário
    
    # Mensagem de welcome para clientes recém conectados
    def getMsgWelcome(self) -> str:
        return f"Bem-vindo ao sistema de compras de ingressos V1.0!\nPara obter ajuda com os comandos, digite: {self.PREFIXO}ajuda\n"
    
    # Resposta do comando ajuda
    def getMsgAjuda(self):
        return f"""Os comandos reconhecidos pelo servidor são: (O servidor não é case-sensitive)
{self.PREFIXO}ajuda -> Obter essa lista de comandos
{self.PREFIXO}listar -> listar os ingressos disponíveis
{self.PREFIXO}escolher -> Escolher qual será o ingresso para a compra
{self.PREFIXO}comprar -> Comprar um novo ingresso
{self.PREFIXO}desconectar -> Desconectar do servidor
    """
    
class Server:    
    HOST: str # Host do serviço
    PORT: str # Porta do serviço
    
    # Conexão que será aberta
    conexao: socket.socket
    
    # Codificações necessárias para o servidor funcionar
    PACKET_SIZE = 1024 # Tamanho em bytes do pacote
    FORMAT = 'utf-8'   # Formato que o pacote será codificado
    
    # Comandos
    PREFIXO = '!' # Prefixo usado para executar comandos
    DISCONNECT_MSG = PREFIXO+'DESCONECTAR' # Mensagem para desconectar o cliente

    # Construtor para criar um servidor
    def __init__(self, host: str, port: int) -> None:
        self.HOST = host
        self.PORT = port
        
        # Inicializando os comandos possíveis para o servidor
        self.comandos = Commands(self.PREFIXO)

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
    def handle(self, cliente: socket.socket, endereco) -> None:
        print(f"Cliente conectado: {endereco[0]}:{endereco[1]}")
        
        # Enviando mensagem de boas-vindas ao cliente
        cliente.send(self.comandos.getMsgWelcome().encode(self.FORMAT))
        
        connected = True
        while connected:
            mensagem = cliente.recv(self.PACKET_SIZE).decode(self.FORMAT)
            
            if mensagem.upper() == self.DISCONNECT_MSG:
                connected = False
                print(f"[CLIENTE]: {endereco[0]} se desconectou!")
                mensagem = 'A desconexão foi um sucesso!'
            
            elif mensagem.upper() == self.PREFIXO+self.comandos.AJUDA:     
                mensagem = f"{self.comandos.getMsgAjuda()}"                
            
            cliente.send(mensagem.encode(self.FORMAT))
        
        cliente.close()
        
    def getNumClientsConnected(self) -> int:
        return threading.active_count()
    
    def close_server(self):
        self.conexao.close()
        print("Server desligado!")

def main() -> None:
    # Abrindo o servidor em todos os dispositivos de rede (Linux)
    server = Server('::', 25665)
    server.open()
    
    clientes = []
    
    while True:
        cliente, endereco = server.conexao.accept()
        
        novo_cliente = threading.Thread(target=server.handle, args=(cliente, endereco))
        novo_cliente.start()
        clientes.append(novo_cliente)


if __name__ == '__main__':
    main()