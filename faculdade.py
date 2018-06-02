from flask import Flask, render_template, request
from flaskext.mysql import MySQL




#instanciar a app e o BD
faculdade = Flask(__name__)
mysql = MySQL(faculdade)
mysql.init_app(faculdade)


# configurar bd
faculdade.config['MYSQL_DATABASE_USER'] = 'root'
faculdade.config['MYSQL_DATABASE_PASSWORD'] = 'root'
faculdade.config['MYSQL_DATABASE_DB'] = 'faculdade'

#criar uma rota para /
@faculdade.route('/')
#metodo que responde a rota
def index():
    return render_template('login.html')

#instancia a app


#criar uma rota para login
@faculdade.route('/login', methods=['POST'])
#metodo que responde a rota
def login():
    param_nome = request.form.get("nome")
    param_senha = request.form.get("senha")


    #cria conexao com o bd
    cursor = mysql.connect().cursor()

    #Submeter o comando SQL
    cursor.execute(f"SELECT * FROM faculdade.usuario WHERE usuario='{param_nome}' AND senha = '{param_senha}';")

    # obtem o retorno
    idusuario = cursor.fetchone()

    #fecha o curso
    cursor.close()

    if idusuario is None:
        return 'Usuário inválido'
    else:
        return render_template('principal.html', nome=param_nome, idusuario=idusuario)

faculdade.run(debug=True)
