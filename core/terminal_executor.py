import subprocess
from utils.logger import log_info, log_erro, log_sucesso

class TerminalExecutor:
    def __init__(self):
        pass

    def executar_comando(self, comando, timeout=30):
        """
        Executa um comando no terminal e retorna stdout, stderr e código de saída.
        """
        log_info(f"🛠️ Executando: {comando}")
        try:
            resultado = subprocess.run(
                comando,
                shell=True,
                capture_output=True,
                text=True,
                timeout=timeout
            )
            stdout = resultado.stdout.strip()
            stderr = resultado.stderr.strip()
            codigo = resultado.returncode

            if codigo == 0:
                log_sucesso(f"✅ Comando executado com sucesso.")
            else:
                log_erro(f"⚠️ Comando retornou erro [{codigo}]: {stderr}")

            return {
                "comando": comando,
                "stdout": stdout,
                "stderr": stderr,
                "codigo": codigo
            }

        except subprocess.TimeoutExpired:
            log_erro(f"⏱️ Timeout ao executar: {comando}")
            return {
                "comando": comando,
                "stdout": "",
                "stderr": "Tempo limite excedido.",
                "codigo": -1
            }

        except Exception as e:
            log_erro(f"❌ Erro inesperado: {e}")
            return {
                "comando": comando,
                "stdout": "",
                "stderr": str(e),
                "codigo": -2
            }