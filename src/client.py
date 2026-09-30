from socket import *

serverName = '127.0.0.1'
serverPort = 12000

def receive_message(clientSocket):
    while True:
        try:
            message = clientSocket.recv(1024).decode('utf-8')
            if not message:
                print("[DESCONECTADO] Servidor encerrou a conexão.")
                break
            print(message, end='')
        except:
            print("[ERRO] Conexão perdida com o servidor.")
            break

clientSocket =  socket(AF_INET, SOCK_STREAM)

try:
    clientSocket.connect((serverName, serverPort))
    print(f"BEM-VINDO(A) AO CHAT!")
    print(f"Digite as suas mensagens (ou '/sair' para fechar):\n")
except Exception as e:
    print(f'[ERRO] Não foi possível conectar ao servidor: {e}')
    sys.exit()

sentence = input('Digite uma frase com letras minúsculas: ')

clientSocket.send(sentence.encode())
modifiedSentence = clientSocket.recv(1024).decode()

print('Do Servidor:', modifiedSentence)

clientSocket.close()
