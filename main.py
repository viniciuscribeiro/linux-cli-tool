# /main.py
import typer
import paramiko

app = typer.Typer()

def execute_remote_command(client: paramiko.SSHClient, command: str, path: str = None):
    """Função auxiliar para executar um comando, opcionalmente em um diretório específico."""
    full_command = f"cd {path} && {command}" if path else command
    print(f"\n$ Executando: '{full_command}'")
    
    stdin, stdout, stderr = client.exec_command(full_command)
    exit_status = stdout.channel.recv_exit_status()
    
    output = stdout.read().decode('utf-8').strip()
    error = stderr.read().decode('utf-8').strip()
    
    if exit_status == 0:
        print(output)
        return output
    else:
        print(f"Erro: {error}")
        return f"Erro ao executar '{command}': {error}"

# ... (o comando 'connect' continua igual)
@app.command()
def connect(
    host: str = typer.Option(..., help="O endereço do host para conectar."),
    username: str = typer.Option(..., help="Nome de usuário para a conexão SSH."),
    password: str = typer.Option(..., prompt=True, hide_input=True, help="Senha para a conexão SSH.")
):
    """Testa a conexão SSH com um servidor remoto."""
    print(f"Tentando conectar com {username}@{host}...")
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        client.connect(hostname=host, username=username, password=password, port=22)
        print("✅ Conexão SSH bem-sucedida!")
    except Exception as e:
        print(f"❌ Falha na conexão: {e}")
    finally:
        client.close()


# ... (o comando 'status' continua igual)
@app.command()
def status(
    host: str = typer.Option(..., help="O endereço do host."),
    username: str = typer.Option(..., help="Nome de usuário SSH."),
    password: str = typer.Option(..., prompt=True, hide_input=True, help="Senha SSH.")
):
    """Busca o status de uptime e memória do servidor remoto."""
    print(f"Buscando status de {username}@{host}...")
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        client.connect(hostname=host, username=username, password=password, port=22)
        uptime = execute_remote_command(client, "uptime -p")
        memory_usage = execute_remote_command(client, "free -h | grep Mem | awk '{print $3\" / \"$2}'")
        print("\n--- Status do Servidor ---")
        print(f"Uptime: {uptime}")
        print(f"Memória (Usada / Total): {memory_usage}")
        print("--------------------------")
    except Exception as e:
        print(f"❌ Falha ao buscar status: {e}")
    finally:
        client.close()

# --- NOVO COMANDO DE DEPLOY ---
@app.command()
def deploy(
    path: str = typer.Argument(..., help="O caminho absoluto para a pasta do projeto no servidor."),
    host: str = typer.Option(..., help="O endereço do host."),
    username: str = typer.Option(..., help="Nome de usuário SSH."),
    password: str = typer.Option(..., prompt=True, hide_input=True, help="Senha SSH.")
):
    """Executa um pipeline de deploy simples em um projeto no servidor."""
    print(f"🚀 Iniciando deploy em {host}...")
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        client.connect(hostname=host, username=username, password=password, port=22)
        
        print("\n--- Pipeline de Deploy ---")
        # Passo 1: Puxar atualizações do Git
        execute_remote_command(client, "git pull", path=path)
        
        # Passo 2: Instalar dependências (simulando um projeto Node.js)
        execute_remote_command(client, "npm install", path=path)
        
        # Passo 3: Reiniciar o serviço (simulando com um 'echo')
        execute_remote_command(client, "echo 'Serviço reiniciado com sucesso!'", path=path)
        
        print("\n✅ Deploy finalizado com sucesso!")
        print("--------------------------")

    except Exception as e:
        print(f"❌ Falha no deploy: {e}")
    finally:
        client.close()

if __name__ == "__main__":
    app()