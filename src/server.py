from socket import *
import threading

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)   
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print('O servidor multithread esta pronto para receber conexoes...')

def handle_client(connectionSocket, addr):
    print(f"[NOVACONEXÃO] Cliente {addr} conectado.")
    try:
        sentence = connectionSocket.recv(1024).decode()
        if sentence:
            print(f"[RECEBIDO de {addr}]: {sentence}")

            capitalizedSentence = sentence.upper()
            connectionSocket.send(capitalizedSentence.encode())
    except Exception as e:
        print(f"[ERRO cliente {addr}]: {e}")
    finally:
        connectionSocket.close()
        print(f"[DESCONECTADO] Cliente {addr} desconectado.")


while True:
    connectionSocket, addr = serverSocket.accept()

    thread = threading.Thread(target=handle_client, args=(connectionSocket, addr))
    thread.daemon = True
    thread.start()