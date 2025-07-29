import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import undetected_chromedriver as uc
from config import CHROME_DATA_DIR, TIMEOUT_CHATGPT
from utils.logger import log_info, log_erro

class ChatGPTBrowser:
    def __init__(self):
        options = uc.ChromeOptions()
        options.add_argument(f"--user-data-dir={CHROME_DATA_DIR}")
        options.add_argument("--disable-blink-features=AutomationControlled")
        self.driver = uc.Chrome(options=options)
        self.driver.get("https://chat.openai.com/")
        
        log_info("🧠 Navegador iniciado. Faça login no ChatGPT.")
        input("🔓 Pressione ENTER quando estiver logado e na tela do chat...")

    def enviar_pergunta(self, pergunta):
        try:
            textarea = self.driver.find_element(By.TAG_NAME, "textarea")
            textarea.click()
            textarea.clear()
            textarea.send_keys(pergunta)
            textarea.send_keys(Keys.ENTER)
            log_info("💬 Pergunta enviada ao ChatGPT.")

            resposta = ""
            start = time.time()
            while time.time() - start < TIMEOUT_CHATGPT:
                time.sleep(1)
                respostas = self.driver.find_elements(By.CLASS_NAME, "markdown")
                if respostas:
                    texto = respostas[-1].text.strip()
                    if texto and texto != resposta:
                        resposta = texto
            return resposta or "⚠️ Nenhuma resposta capturada."
        except Exception as e:
            log_erro(f"Erro ao enviar pergunta: {e}")
            return "❌ Erro na comunicação com o ChatGPT Web."

    def fechar(self):
        try:
            self.driver.quit()
            log_info("🧹 Navegador encerrado com sucesso.")
        except Exception as e:
            log_erro(f"Erro ao encerrar navegador: {e}")