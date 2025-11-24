from flask import Blueprint, jsonify, request

from servicos.funcionario import FuncionarioDatabase
funcionario_blueprint = Blueprint("funcionario", __name__)

# Retorna um Funcionário
@funcionario_blueprint.route("/funcionario", methods=["GET"])
def get_funcionario():    
    # Parâmetros - Filtra por cpf e nome
    cpf = request.args.get("cpf", "")
    nome = request.args.get("nome", "")
    return jsonify(FuncionarioDatabase().get_funcionario(cpf, nome)), 200

# Insere um Funcionário novo
@funcionario_blueprint.route("/funcionario", methods=["POST"])
def insere_funcionario():
    json = request.get_json()
    cpf = json.get("CPF")
    nome = json.get("nome")
    registro = FuncionarioDatabase().regristra_funcionario(cpf, nome)

    if not registro:
        return jsonify("Não foi possível registrar o funcionário"), 400

    return jsonify("Funcionário registrado com sucesso!"), 200

# Remove um Funcionário
@funcionario_blueprint.route("/funcionario", methods=["DELETE"])
def deleta_funcionario():
    cpf = request.args.get("cpf", "")
    nome = request.args.get("nome", "")
    delete = FuncionarioDatabase().remove_funcionario(cpf, nome)

    if not delete:
        return jsonify("Não foi possível solicitar a remoção do funcionário"), 400

    return jsonify("Remoção do funcionário solicitada com sucesso!"), 200

# Atualiza um Cliente
@funcionario_blueprint.route("/funcionario", methods=["PUT"])
def atualiza_funcionário():
    cpf = request.args.get("cpf", "")
    nome = request.args.get("nome", "")
    cpf_novo = request.args.get("cpf_novo", "")
    nome_novo = request.args.get("nome_novo", "")
    delete = FuncionarioDatabase().atualiza_funcionario(cpf, cpf_novo, nome, nome_novo)

    if not delete:
        return jsonify("Não foi possível solicitar a atualização do funcionário"), 400

    return jsonify("Atualização do funcionário solicitada com sucesso!"), 200