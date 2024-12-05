# Configuração do Flask e rotas principais

from flask import Flask, render_template, request, redirect, url_for
from models import db, Task

# Inicializa o aplicativo Flask.
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db' # Define o banco de dados SQLite chamado tasks.db como o backend de armazenamento.
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # Desabilita notificações de mudanças para melhorar desempenho.
db.init_app(app) # Associa o banco de dados ao aplicativo Flask.

# Exibe a página principal com a lista de tarefas.
@app.route("/")
def index():
    tasks = Task.query.all() # Consulta todas as tarefas no banco de dados.
    return render_template('index.html', tasks=tasks) # Renderiza a página HTML index.html e passa a lista de tarefas para ela.

# Permite adicionar novas tarefas ao banco de dados.
@app.route('/add', methods=['GET', 'POST']) # Suporta os métodos HTTP GET e POST
def add_task():
    if request.method == 'POST':
        title = request.form['title'] # Captura o valor do campo title no formulário
        new_task = Task(title=title) # Cria uma nova tarefa com o título recebido
        db.session.add(new_task) # Adiciona a nova tarefa à sessão do banco
        db.session.commit() # Salva a tarefa no banco
        return redirect(url_for('index')) # Redireciona o usuário para a página inicial após salvar
    return render_template('add_task.html')

if __name__ == '__main__': # Garante que o código só será executado se o arquivo for o principal
    with app.app_context(): # Cria o contexto necessário para interagir com o banco de dados
        db.create_all() # Cria as tabelas no banco de dados se ainda não existirem
    app.run(debug=True) # Inicia o servidor Flask no modo de depuração