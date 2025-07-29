from flask import Flask
from routes.chat_routes import chat_blueprint

def create_app():
    app = Flask(__name__)

    # Registrando as rotas do chat
    app.register_blueprint(chat_blueprint)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=5000)