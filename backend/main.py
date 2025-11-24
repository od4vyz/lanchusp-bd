from flask import Flask, jsonify
from flask_cors import CORS
from rotas.cliente import cliente_blueprint

app = Flask(__name__)
# Permite qualquer IP acessar a database
CORS(app, origins="*")

@app.route("/", methods={"GET"})
def get_autor():
    return jsonify("tudo certo"), 200

# Registro das Rotas
app.register_blueprint(cliente_blueprint)
app.run("0.0.0.0", port=8000, debug=False)