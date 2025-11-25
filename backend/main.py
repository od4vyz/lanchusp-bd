from flask import Flask, jsonify, render_template
from flask_cors import CORS
from servicos.lanchonete import LanchoneteDatabase
from rotas.cliente import cliente_blueprint
from rotas.funcionario import funcionario_blueprint
from rotas.lanchonete import lanchonete_blueprint
from rotas.item import item_blueprint
from rotas.receita import receita_blueprint
from rotas.produto_pronto import produtoPronto_blueprint

app = Flask(__name__)
# Permite qualquer IP acessar a database
CORS(app, origins="*")

@app.route("/", methods={"GET"})
def home():
    lanchonetes = LanchoneteDatabase().get_lanchonete("", "")

    return render_template("index.html", lanchonetes=lanchonetes), 200

# Registro das Rotas
app.register_blueprint(cliente_blueprint)
app.register_blueprint(funcionario_blueprint)
app.register_blueprint(lanchonete_blueprint)
app.register_blueprint(item_blueprint)
app.register_blueprint(receita_blueprint)
app.register_blueprint(produtoPronto_blueprint)
app.run("0.0.0.0", port=8000, debug=False)