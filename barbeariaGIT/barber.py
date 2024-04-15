from flask import Flask, render_template

app = Flask(__barberconnet__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')

@app.route('/agendamento')
def agendamento():
    return render_template('agendamento.html')

if __name__ == '__main__':
    app.run(debug=True)