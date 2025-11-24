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