# Multi-Client TCP Chat System in Python

Este projeto consiste em um sistema de chat multiusuário baseado no protocolo de camada de transporte **TCP**, desenvolvido em Python utilizando a API nativa de **Sockets** e **Threads**. 

O desenvolvimento do sistema foi dividido em fases incrementais de complexidade, devidamente marcadas e versionadas com **Git Tags**.

---

## 🛠️ Tecnologias Utilizadas

* **Linguagem**: Python 3.x
* **Redes**: Sockets TCP (`socket` module)
* **Concorrência**: Programação Multithreaded (`threading` module)
* **Versionamento**: Git & GitHub

---

## 🚀 Estrutura do Projeto e Fases

O projeto evoluiu em 3 etapas principais:

### 📍 Fase 1: Comunicação Básica Mono-cliente (Tag: `v1.0.0-fase1`)
* Implementação base da arquitetura Cliente-Servidor via socket TCP.
* O servidor atende uma única requisição por vez, recebe uma mensagem em texto simples, converte para maiúsculas e devolve a resposta ao cliente.

### 📍 Fase 2: Servidor Multithread (Tag: `v2.0.0-fase2`)
* Atualização do `server.py` com a biblioteca `threading`.
* A chamada `accept()` roda em loop contínuo e dispara uma *thread* separada para tratar a conexão individual de cada cliente sem bloquear novas conexões de rede.

### 📍 Fase 3: Chat Multiusuário com Broadcast (Tag: `v3.0.0-fase3`)
* **Retransmissão (Broadcast)**: As mensagens enviadas por um participante são formatadas com o identificador de IP:Porta e retransmitidas para todos os outros participantes ativos.
* **Notificações**: O servidor envia avisos globais no chat quando um novo participante entra ou sai da sala.
* **I/O Não-Bloqueante no Cliente**: O `client.py` utiliza duas *threads* (uma para escutar o servidor e outra para ler a entrada do teclado) para evitar o travamento da interface.
* **Encerramento Gracioso**: Suporte ao comando `/sair` com tratamento da flag `running` para fechar os sockets sem disparar exceções de rede no terminal.

---

## 📂 Estrutura de Arquivos

```text
chat-sockets-python/
│
├── .git/
├── docs/            # Documentação complementar e evidências
├── src/
│   ├── server.py    # Servidor de Chat Multithread (TCP)
│   └── client.py    # Cliente de Chat com Dual-Thread
│
├── .gitattributes
├── .gitignore
└── README.md