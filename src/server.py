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
    client_id = f"{addr[0]}:{addr[1]}"
    print(f"[ENTRADA] Participante {client_id} entrou no chat.")

    join_msg = f"📢 [SERVIDOR]: O participante {client_id} entrou no chat!\n"
    broadcast(join_msg.encode('utf-8'), connectionSocket)

    while True:
        try:
            message = connectionSocket.recv(1024)
            if not message:
                break
            print(f"[{client_id}]: {message.decode('utf-8')}")
            formatedmessage = f"[{client_id}]: {message.decode('utf-8')}\n"
            broadcast(formatedmessage.encode('utf-8'), connectionSocket)
        except:
            break

    print(f"[SAÍDA] Participante {client_id} saiu do chat.")
    remove_client(connectionSocket)
    
    leave_msg = f"📢 [SERVIDOR]: O participante {client_id} saiu do chat!\n"
    broadcast(leave_msg.encode('utf-8'))

while True:
    connectionSocket, addr = serverSocket.accept()

    thread = threading.Thread(target=handle_client, args=(connectionSocket, addr))
    thread.daemon = True
    thread.start()