#Importar bibliotacas
from flask import Flask, render_template, redirect, url_for

# Dar apelido a aplicação (app)
app = Flask(__name__)

@app.route('/')
def hello_world():
    return redirect('/index')

@app.route('/index')
def home():
    return render_template('index.html')

@app.route('/pessoa')
def pessoa():
    return render_template('pessoa.html')

# Executar aplicação
if __name__ == '__main__':
    app.run(debug=True)
