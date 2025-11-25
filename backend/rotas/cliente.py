from flask import Blueprint, jsonify, request

from servicos.cliente import ClienteDatabase

cliente_blueprint = Blueprint("cliente", __name__)

# Retorna um Cliente
@cliente_blueprint.route("/cliente", methods=["GET"])
def get_cliente():    
    # Parâmetros - Filtra por cpf, nome ou número do cliente
    cpf = request.args.get("cpf", "")
    nome = request.args.get("nome", "")
    id = request.args.get("id", "")
    return jsonify(ClienteDatabase().get_cliente(cpf, nome, id)), 200

# Insere um Cliente novo
@cliente_blueprint.route("/cliente", methods=["POST"])
def insere_cliente():
    json = request.get_json()
    cpf = json.get("CPF")
    nome = json.get("nome")
    registro = ClienteDatabase().regristra_cliente(cpf, nome)

    if not registro:
        return jsonify("Não foi possível registrar o cliente"), 400

    return jsonify("Cliente registrado com sucesso!"), 200

# Remove um Cliente
@cliente_blueprint.route("/cliente", methods=["DELETE"])
def deleta_cliente():
    cpf = request.args.get("cpf", "")
    nome = request.args.get("nome", "")
    id = request.args.get("id", "")
    delete = ClienteDatabase().remove_cliente(cpf, nome, id)

    if not delete:
        return jsonify("Não foi possível solicitar a remoção do cliente"), 400

    return jsonify("Remoção do Cliente solicitada com sucesso!"), 200

# Atualiza um Cliente
@cliente_blueprint.route("/cliente", methods=["PUT"])
def atualiza_cliente():
    cpf = request.args.get("cpf", "")
    nome = request.args.get("nome", "")
    id = request.args.get("id", "")
    cpf_novo = request.args.get("cpf_novo", "")
    nome_novo = request.args.get("nome_novo", "")
    delete = ClienteDatabase().atualiza_cliente(cpf, cpf_novo, nome, nome_novo, id)

    if not delete:
        return jsonify("Não foi possível solicitar a atualização do cliente"), 400

    return jsonify("Atualização do Cliente solicitada com sucesso!"), 200