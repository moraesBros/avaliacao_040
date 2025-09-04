from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    # Pega data e hora atuais
    now = datetime.now()
    
    # Formata para strings compatíveis com <input type="date"> e <input type="time">
    data_atual = now.strftime('%Y-%m-%d')
    hora_atual = now.strftime('%H:%M:%S')

    # Renderiza o template, passando as variáveis
    return render_template(
        'index.html',
        data_atual=data_atual,
        hora_atual=hora_atual
    )

if __name__ == '__main__':
    app.run(debug=True)
