from flask import Blueprint, request, jsonify
from core.browser_api import ChatGPTBrowser
from utils.helpers import (
    validar_json_requisicao,
    formatar_resposta_json,
    montar_prompt,  # ✅ Nova importação
)
from utils.logger import log_info, log_erro, log_sucesso

# Instância única do navegador
chatgpt = ChatGPTBrowser()

# Criando o blueprint de rotas
chat_blueprint = Blueprint("chat_routes", __name__)

@chat_blueprint.route("/chat", methods=["POST"])
def chat():
    data = request.get_json(force=True)
    valido, erro_msg = validar_json_requisicao(data, "pergunta")

    if not valido:
        log_erro(f"Requisição inválida: {erro_msg}")
        return jsonify({"erro": erro_msg}), 400

    # ✅ Adiciona contexto Termux à pergunta
    pergunta = montar_prompt(data["pergunta"])
    log_info(f"🔍 Pergunta contextualizada: {pergunta}")

    try:
        resposta = chatgpt.enviar_pergunta(pergunta)
        log_sucesso("✅ Resposta obtida com sucesso.")
        return jsonify(formatar_resposta_json(resposta))
    except Exception as e:
        log_erro(f"Erro ao enviar pergunta: {e}")
        return jsonify({"erro": "Falha ao comunicar com o ChatGPT"}), 500

@chat_blueprint.route("/fechar", methods=["POST"])
def fechar():
    try:
        chatgpt.fechar()
        log_info("🧹 Navegador fechado com sucesso.")
        return jsonify({"status": "Navegador encerrado."})
    except Exception as e:
        log_erro(f"Erro ao fechar navegador: {e}")
        return jsonify({"erro": "Não foi possível fechar o navegador."}), 500
