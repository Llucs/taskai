import time
import json

def validar_json_requisicao(data, chave):
    """
    Valida se a chave existe no JSON recebido.
    """
    if chave not in data or not data[chave].strip():
        return False, f"❌ Erro: Chave '{chave}' ausente ou vazia no JSON."
    return True, ""

def temporizador_segundos(segundos):
    """
    Espera o número de segundos desejado com indicador.
    """
    print(f"⏳ Esperando {segundos} segundos...")
    time.sleep(segundos)

def formatar_resposta_json(texto):
    """
    Gera um dicionário padrão de resposta para a API.
    """
    return {"resposta": texto.strip()}

def carregar_config_local(caminho):
    """
    Carrega configurações JSON locais.
    """
    try:
        with open(caminho, "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    except Exception as e:
        print(f"⚠️ Erro ao carregar config: {e}")
        return {}

def montar_prompt(pergunta_usuario):
    """
    Insere contexto Termux na pergunta enviada ao ChatGPT.
    """
    contexto = (
        "Você está dentro do ambiente Termux no Android. "
        "Responda APENAS com o comando bash necessário para executar a tarefa solicitada. "
        "Sem explicações, formatações ou comentários."
    )
    return f"{contexto}\nTarefa: {pergunta_usuario}"
