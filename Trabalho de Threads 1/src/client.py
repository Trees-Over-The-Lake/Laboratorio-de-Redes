import socket

class Cliente:
    IP:   str # IP do servidor para conectar
    PORT: str # Porta do servidor 

    # Socket que guarda a conexão com o servidor
    conexao: socket.socket 
    
    PACKET_SIZE = 1024 # Tamanho em bytes do pacote
    FORMAT = 'utf-8'   # Formato que o pacote será codificado
    
    # Comandos
    PREFIXO = '!' # Prefixo usado para executar comandos
    DISCONNECT_MSG = PREFIXO+'DESCONECTAR' # Mensagem para desconectar o cliente

    # Criando um novo cliente
    def __init__(self, ip, porta) -> None:
        self.IP = ip
        self.PORT = porta
        
    # Conectar em um servidor
    def conectar(self) -> None:
        # Tentar logar por IPv4
        try:
            self.conexao = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   
            self.conexao.connect((self.IP, self.PORT))
            return
        
        # Tentar logar por IPv6
        except:
            try:
                self.conexao = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)   
                self.conexao.connect((self.IP, self.PORT))
                return
            
            # Ip Inválido!        
            except:
                print('Impossível conectar ao servidor, tente outro IP!')

    # Gerênciar cliente
    def handle(self):
        conectado = True
        print(self.conexao.recv(self.PACKET_SIZE).decode(self.FORMAT))
        
        while conectado:
            # Enviando mensagem para o servidor
            mensagem = input("> ")
            
            # Enviando a mensagem
            self.conexao.send(mensagem.encode(self.FORMAT))
            
            # Desconectar cliente
            if mensagem.upper() == self.DISCONNECT_MSG:
                conectado = False
               
            mensagem = self.conexao.recv(self.PACKET_SIZE).decode(self.FORMAT)
            print(f"[SERVER]: {mensagem}")
    
    # Fechar conexão
    def fechar(self) -> None:
        self.conexao.close()       
        

def main() -> None:
    cliente = Cliente("::1", 25665)
    cliente.conectar()
    cliente.handle()
    cliente.fechar()
        

if __name__ == '__main__':
    main()