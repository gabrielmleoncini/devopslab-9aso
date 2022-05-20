from flask import Flask

app = Flask(__name__)

@app.route("/")
def pagina_inicial():
    return "Alteracao Mensagem - Gabriel Mazzi Leoncini"

if __name__ == '__main__':
    app.run()