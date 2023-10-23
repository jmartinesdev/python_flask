from flask import Flask, render_template

app = Flask(__name__)


# criar a primeira pagina do site
# route -> meusite.com/usuarios/contatos ou /
# funcao -> é o que voce quer exibir naquela pagina
# templates

@app.route("/")
def homepage():
    return render_template("homepage.html")

@app.route("/contatos")
def contatos():
    return render_template("contatos.html")

@app.route("/usuarios/<nome_usuario>")
def usuarios(nome_usuario):
    return render_template("usuarios.html", nome_usuario=nome_usuario)

# colocar o site no ar
if __name__ == "__main__":
    app.run(debug=True)