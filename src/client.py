from socket import *
import threading
import sys

serverName = '127.0.0.1'
serverPort = 12000

running = True

def receive_message(clientSocket):
    while True:
        try:
            message = clientSocket.recv(1024).decode('utf-8')
            if not message:
                print("[DESCONECTADO] Servidor encerrou a conexão.")
                break
            print(message, end='', flush=True)
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
    
receive_thread = threading.Thread(target=receive_message, args=(clientSocket,))
receive_thread.daemon = True
receive_thread.start()

while True:
    try:
        msg = input()
        if msg.lower() == '/sair':
            break
        if msg.strip():
            clientSocket.send(f"{msg}\n".encode('utf-8'))
    except (KeyboardInterrupt, EOFError):
        break

clientSocket.close()
print("Você saiu do chat.")
