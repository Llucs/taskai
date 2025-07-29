🧠 TaskAI – Automação Inteligente com ChatGPT no Termux

TaskAI é uma assistente de automação baseada em Python que usa o ChatGPT Web de forma não-oficial, via automação de navegador, para interpretar tarefas, gerar comandos e executá-los automaticamente no ambiente Termux Android.

> Não consome créditos da OpenAI, não depende da API oficial, e roda localmente com total controle.

---

⚙️ Funcionalidades

- 🤖 Integração via navegador com o ChatGPT Web (API caseira)
- 🔐 Sessão persistente com perfil de usuário no Chrome
- 📡 API REST via Flask para receber requisições externas
- 📟 Execução de comandos diretamente no Termux com subprocess
- 🧩 Logs coloridos e estrutura modular para escalar
- 🛡️ Validação semântica das perguntas e segurança na execução

---

🚀 Como Funciona

1. O navegador é iniciado e se conecta ao ChatGPT Web
2. Uma pergunta é enviada via /chat, com contexto do Termux embutido
3. O ChatGPT responde com um comando bash limpo
4. O comando é capturado e executado no ambiente local
5. A saída é retornada como JSON pela API

---

📁 Estrutura do Projeto

`plaintext
taskai/
├── app.py                  # Inicia o Flask e registra as rotas
├── config.py               # Configurações globais (timeout, diretórios)
├── core/
│   ├── browser_api.py      # Automação do navegador com ChatGPT Web
│   └── terminal_executor.py# Execução de comandos reais no Termux
├── routes/
│   └── chat_routes.py      # Endpoints /chat e /fechar
├── utils/
│   ├── logger.py           # Logs coloridos e padronizados
│   └── helpers.py          # Validadores, formatadores e prompt builder
└── static/
    └── chrome_data/        # Sessão persistente do navegador
`

(Tentei colocar aqui mas deve estar toda torta 😅)
---

📦 Instalação

`bash
git clone https://github.com/Llucs/taskai
cd taskai
pip install -r requirements.txt
python app.py
`

Após iniciar, o navegador será aberto. Faça login no ChatGPT Web e pressione ENTER no terminal quando estiver na tela principal.

---

📡 Usando a API

`bash
curl -X POST http://localhost:5000/chat \
     -H "Content-Type: application/json" \
     -d '{"pergunta": "Instalar curl no Termux"}'
`

✅ Retorno esperado:

`json
{
  "resposta": "pkg install curl"
}
`

---

🧠 Prompt com Consciência de Ambiente

Toda pergunta enviada ao ChatGPT é automaticamente enriquecida com:

> "Você está dentro do ambiente Termux no Android. Responda APENAS com o comando bash necessário para executar a tarefa solicitada. Sem explicações, formatações ou comentários."

Isso garante que o ChatGPT se comporte como se estivesse dentro do terminal.

---

📌 Próximos Passos

- 🧵 Fila de execução para múltiplas requisições
- 🗂️ Cache local para comandos repetidos
- 🔐 Autenticação na API
- ⚡ Detecção inteligente do fim da resposta via DOM

---

👨‍💻 Autor

Projeto criado por Leandro com suporte da TaskAI.  
Feito para programadores que querem automatizar com estilo. 😎

---

⚠️ Aviso Legal

Este projeto utiliza automação de navegador para interagir com o site do ChatGPT e não é afiliado à OpenAI. Use com responsabilidade.