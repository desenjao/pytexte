from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "E aí, meu brother! Servidor tá no ar! �"

if __name__ == '__main__':
    app.run(debug=True)