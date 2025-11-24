from flask import Blueprint, jsonify, request

from servicos.cliente import ClienteDatabase

cliente_blueprint = Blueprint("cliente", __name__)

# Retorna um Cliente
@cliente_blueprint.route("/cliente", methods=["GET"])
def get_cliente():    
    # Parâmetros - Filtra por cpf, nome ou número do cliente
    cpf = request.args.get("cpf", "")
    nome = request.args.get("nome", "")
    numero_cliente = request.args.get("numero_cliente", "")
    return jsonify(ClienteDatabase().get_cliente(cpf, nome, numero_cliente)), 200

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

# Remove um Cliente - Ainda não funciona
@cliente_blueprint.route("/cliente", methods=["DELETE"])
def deleta_cliente():
    cpf = request.args.get("cpf", "")
    nome = request.args.get("nome", "")
    numero_cliente = request.args.get("numero_cliente", "")
    registro = ClienteDatabase().remove_cliente(cpf, nome, numero_cliente)

    if not registro:
        return jsonify("Não foi possível remover o cliente"), 400

    return jsonify("Cliente removido com sucesso!"), 200