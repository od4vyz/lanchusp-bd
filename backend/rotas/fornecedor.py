from flask import Blueprint, jsonify, request

from servicos.fornecedor import FornecedorDatabase

fornecedor_blueprint = Blueprint("fornecedor", __name__)

# Retorna um Fornecedor
@fornecedor_blueprint.route("/fornecedor", methods=["GET"])
def get_fornecedor():    
    # Parâmetros - Filtra por localizacao e nome
    localizacao = request.args.get("localizacao", "")
    nome = request.args.get("nome", "")
    return jsonify(FornecedorDatabase().get_fornecedor(localizacao, nome)), 200

# Insere um Fornecedor novo
@fornecedor_blueprint.route("/fornecedor", methods=["POST"])
def insere_fornecedor():
    json = request.get_json()
    localizacao = json.get("localizacao")
    nome = json.get("nome")
    registro = FornecedorDatabase().regristra_fornecedor(localizacao, nome)

    if not registro:
        return jsonify("Não foi possível registrar o fornecedor"), 400

    return jsonify("Fornecedor registrada com sucesso!"), 200

# Remove um Fornecedor
@fornecedor_blueprint.route("/fornecedor", methods=["DELETE"])
def deleta_fornecedor():
    localizacao = request.args.get("localizacao", "")
    nome = request.args.get("nome", "")
    delete = FornecedorDatabase().remove_fornecedor(localizacao, nome)

    if not delete:
        return jsonify("Não foi possível solicitar a remoção do fornecedor"), 400

    return jsonify("Remoção do fornecedor solicitada com sucesso!"), 200