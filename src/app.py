# app.py
from flask import Flask, render_template
from persistencia import Persistencia

app = Flask(__name__)
persistencia = Persistencia()

@app.route("/")
def index():
    tarefas = persistencia.listar_tarefas()
    return render_template('index.html', tarefas=tarefas)

if __name__ == "__main__":
    app.run(debug=True)
