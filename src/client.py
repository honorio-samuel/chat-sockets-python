from socket import *

serverName = '127.0.0.1'
serverPort = 12000

clientSocket =  socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

sentence = input('Digite uma frase com letras minúsculas: ')

clientSocket.send(sentence.encode())
modifiedSentence = clientSocket.recv(1024).decode()

print('Do Servidor:', modifiedSentence)

clientSocket.close()
