# Linux Server Manager CLI 🐧💻

<br>

Uma ferramenta de linha de comando (CLI) construída em Python para automatizar o gerenciamento e deploy de aplicações em servidores Linux via SSH.

**Exemplo de Uso:**

```bash
# Checar o status de um servidor
$ python main.py status --host 127.0.0.1 --username vinicius

# Realizar o deploy de uma aplicação
$ python main.py deploy /home/vinicius/meu-app --host 127.0.0.1 --username vinicius
```

-----

## 📖 Sobre o Projeto

O **Linux Server Manager CLI** é uma ferramenta de automação desenvolvida para simplificar tarefas comuns de administração de servidores. Em vez de se conectar manualmente via SSH e digitar uma série de comandos repetitivos, esta CLI permite encapsular esses fluxos de trabalho em comandos simples e diretos.

Este projeto demonstra habilidades em:

  - Desenvolvimento de ferramentas de linha de comando com Python.
  - Automação de tarefas de infraestrutura (DevOps).
  - Comunicação de rede segura utilizando o protocolo SSH.

-----

## ✨ Funcionalidades

Atualmente, a ferramenta suporta os seguintes comandos:

  - **`connect`**: Testa a autenticação e a conexão SSH com um servidor alvo.
  - **`status`**: Conecta ao servidor e retorna um resumo da "saúde" do sistema, incluindo uptime e uso de memória.
  - **`deploy`**: Automatiza um pipeline de deploy simples, executando uma sequência de comandos (`git pull`, `npm install`, etc.) em um diretório de projeto no servidor remoto.

-----

## 命令行 Como Usar (API da CLI)

Todos os comandos exigem as credenciais do servidor, que podem ser passadas como opções. A senha será solicitada de forma segura.

### Checar Status do Servidor

```bash
python main.py status --host <ip_do_servidor> --username <seu_usuario>
```

### Realizar Deploy

```bash
python main.py deploy <caminho_do_app_no_servidor> --host <ip_do_servidor> --username <seu_usuario>
```

Exemplo:

```bash
python main.py deploy /home/user/my-node-app --host 192.168.1.10 --username user
```

-----

## 🚀 Tecnologias Utilizadas

  - **Python**
  - **Typer**: Para a criação da interface de linha de comando de forma rápida e moderna.
  - **Paramiko**: Para a implementação do cliente SSH que se conecta e executa os comandos remotos.

-----

## ⚙️ Instalação e Configuração

**1. Ambiente do Cliente (onde a CLI roda):**

```bash
# Clone o repositório
git clone https://github.com/viniciuscribeiro/linux-cli.git # Substitua pela URL correta
cd linux-cli

# Crie e ative o ambiente virtual
python -m venv venv
# Windows: .\venv\Scripts\Activate.ps1
# Linux/macOS: source venv/bin/activate

# Instale as dependências
pip install "typer[all]" paramiko
```

**2. Ambiente do Servidor (o Linux que será gerenciado):**
O servidor alvo precisa ter um servidor OpenSSH instalado e rodando.

```bash
# Em servidores baseados em Debian/Ubuntu
sudo apt update
sudo apt install openssh-server
sudo service ssh start
```

-----

## 📞 Contato

**Vinicius Cordeiro Ribeiro**

  - **Email:** viniciuscordeiroribeiro@gmail.com
  - **LinkedIn:** [https://www.linkedin.com/in/viniciuscordeiroribeiro/](https://www.linkedin.com/in/viniciuscordeiroribeiro/)
  - **GitHub:** [https://github.com/viniciuscribeiro](https://github.com/viniciuscribeiro)
