import datetime

# Códigos ANSI para cores
class Cor:
    INFO = "\033[94m"
    SUCESSO = "\033[92m"
    AVISO = "\033[93m"
    ERRO = "\033[91m"
    RESET = "\033[0m"

def log_info(mensagem):
    print(f"{Cor.INFO}[INFO {timestamp()}] {mensagem}{Cor.RESET}")

def log_sucesso(mensagem):
    print(f"{Cor.SUCESSO}[✔️ SUCESSO {timestamp()}] {mensagem}{Cor.RESET}")

def log_aviso(mensagem):
    print(f"{Cor.AVISO}[⚠️ AVISO {timestamp()}] {mensagem}{Cor.RESET}")

def log_erro(mensagem):
    print(f"{Cor.ERRO}[❌ ERRO {timestamp()}] {mensagem}{Cor.RESET}")

def timestamp():
    return datetime.datetime.now().strftime("%H:%M:%S")