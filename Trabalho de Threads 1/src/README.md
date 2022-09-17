# Sistema de compras de ingressos V1.0

Este é um programa simples para o back-end de um sistema de compras de ingresso que usa apenas as bibliotecas nativas do python, não sendo necessário importar nada de fora (pip, por exemplo).

## Como usar:
### Servidor:

Há duas maneiras de iniciar o servidor:

```bash
python3 server.py
```

Com essa opção, será perguntado quais os eventos, preços e quantidade de ingressos ainda tem disponível, no momento em que o servidor for iniciado. Caso queira adiantar a inicialização do servidor, pode-se escrever em um arquivo como o arquivo de exemplo que foi deixado e redirecionar  a entrada para o servidor, dessa forma:

```bash
python3 server.py < eventos_example.txt
```


### Cliente:

```bash
python3 client.py
```

## Estrutura do servidor

O servidor possui um loop principal ao qual recebe todas as requisições de conexão, aceita-as e depois move para ser processada em outra thread. Nessa outra thread o cliente sempre terá uma sessão exclusica para ele enviar e receber mensagens ao servidor. Caso o cliente deseje comprar algum ingresso todas as compras serão congeladas para os outros clientes. Assim que terminar as compras, será liberada a compra para os outros clientes. Todos os comandos que forem executados, que não sejam o de comprar estarão sempre liberados, mesmo que algum cliente esteja efetuando uma compra.

## License
[MIT](https://choosealicense.com/licenses/mit/)