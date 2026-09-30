from socket import *
import threading

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)   
serverSocket.bind(('', serverPort))
serverSocket.listen()

clients = []

def broadcast(message, sender_socket=None):
    for client in clients:
        if client != sender_socket:
            try:
                client.send(message)
            except:
                remove_client(client)

def remove_client(client_socket):
    if client_socket in clients:
        clients.remove(client_socket)
        try:
            client_socket.close()
        except:
            pass

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