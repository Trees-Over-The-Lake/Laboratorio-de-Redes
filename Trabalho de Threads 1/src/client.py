import socket

class Cliente:
    IP:   str # IP do servidor para conectar
    PORT: str # Porta do servidor 

    # Socket que guarda a conexão com o servidor
    conexao: socket.socket 

    # Criando um novo cliente
    def __init__(self, ip, porta) -> None:
        self.IP = ip
        self.PORT = porta
        
    # Conectar em um servidor
    def conectar(self) -> None:
        self.conexao = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)   
        self.conexao.connect((self.IP, self.PORT))
        
    # Fechar conexão
    def fechar(self) -> None:
        self.conexao.close()       
        

def main() -> None:
    cliente = Cliente("::1", 25665)
    cliente.conectar()
    
    
    print(f"Conectei ao servidor!")
    #input("Digite qualquer coisa para sair")
    cliente.fechar()
        

if __name__ == '__main__':
    main()