from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    now = datetime.now()

    # Formata mês em inglês, dia como número, hora em AM/PM
    # Resultado exemplo: "September 2, 2025  8:15 PM"
    data_hora = now.strftime("%B %-d, %Y %I:%M %p")  
    # Para Windows, use "%B %#d, %Y %I:%M %p" ou rstrip em Python:
    # data_hora = now.strftime("%B %d, %Y %I:%M %p").lstrip("0").replace(" 0", " ")

    return render_template('index.html', data_hora=data_hora)

if __name__ == '__main__':
    app.run(debug=True)
