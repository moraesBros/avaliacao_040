from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    # Procura por "index.html" dentro da pasta "templates"
    return render_template('index.html')


if __name__ == '__main__':
    # debug=True ativa recarga automática e mostra erros no navegador
    app.run(debug=True)
