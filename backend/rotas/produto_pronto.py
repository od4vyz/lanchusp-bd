from flask import Blueprint, jsonify, request

from servicos.produto_pronto import ProdutoProntoDatabase

produtoPronto_blueprint = Blueprint("produtoPronto", __name__)

# Retorna um Produto_Pronto
@produtoPronto_blueprint.route("/produtoPronto", methods=["GET"])
def get_produtoPronto():    
    # Parâmetros - Filtra por nome ou categoria do Produto_Pronto
    nome = request.args.get("nome", "")
    categoria = request.args.get("categoria", "")
    return jsonify(ProdutoProntoDatabase().get_produtoPronto(nome, categoria)), 200

# Insere um Produto_Pronto novo
@produtoPronto_blueprint.route("/produtoPronto", methods=["POST"])
def insere_produtoPronto():
    json = request.get_json()
    nome = json.get("Nome_Item")
    categoria = json.get("Categoria")
    registro = ProdutoProntoDatabase().regristra_produtoPronto(nome, categoria)

    if not registro:
        return jsonify("Não foi possível registrar o Produto Pronto"), 400

    return jsonify("Produto Pronto com sucesso!"), 200

# Remove um Produto_Pronto
@produtoPronto_blueprint.route("/produtoPronto", methods=["DELETE"])
def deleta_produtoPronto():
    nome = request.args.get("nome", "")
    categoria = request.args.get("categoria", "")
    delete = ProdutoProntoDatabase().remove_produtoPronto(nome, categoria)

    if not delete:
        return jsonify("Não foi possível solicitar a remoção do Produto Pronto"), 400

    return jsonify("Remoção do Produto Pronto solicitada com sucesso!"), 200

# Atualiza um Produto_Pronto
@produtoPronto_blueprint.route("/produtoPronto", methods=["PUT"])
def atualiza_produtoPronto():
    nome = request.args.get("nome", "")
    nome_novo = request.args.get("nome_novo", "")
    categoria_nova = request.args.get("categoria_nova", "")
    delete = ProdutoProntoDatabase().atualiza_produtoPronto(nome, nome_novo, categoria_nova)

    if not delete:
        return jsonify("Não foi possível solicitar a atualização do Produto Pronto"), 400

    return jsonify("Atualização do Produto Pronto solicitada com sucesso!"), 200