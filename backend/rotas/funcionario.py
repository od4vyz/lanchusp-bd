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

# Retorna os Funcionários de uma Lanchonete
@funcionario_blueprint.route("/funcionarios_campus", methods=["GET"])
def get_funcionarios_lanchonete():    
    # Parâmetros - Filtra por lanchonete
    campus = request.args.get("campus", "")
    return jsonify(FuncionarioDatabase().get_funcionarios_lanchonete(campus)), 200


# Retorna a média salarial dos Funcionários por cargo
@funcionario_blueprint.route("/media_salarial_cargo", methods=["GET"])
def get_media_salarial_cargo():    
    return jsonify(FuncionarioDatabase().get_media_salarial_cargo()), 200

# Retorna os Funcionários Coringas
@funcionario_blueprint.route("/funcionarios_coringas", methods=["GET"])
def get_funcionarios_coringas():    
    return jsonify(FuncionarioDatabase().get_funcionarios_coringas()), 200

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

# Atualiza um Funcionario
@funcionario_blueprint.route("/funcionario", methods=["PUT"])
def atualiza_funcionario():
    cpf = request.args.get("cpf", "")
    nome = request.args.get("nome", "")
    cpf_novo = request.args.get("cpf_novo", "")
    nome_novo = request.args.get("nome_novo", "")
    update = FuncionarioDatabase().atualiza_funcionario(cpf, cpf_novo, nome, nome_novo)

    if not update:
        return jsonify("Não foi possível solicitar a atualização do funcionário"), 400

    return jsonify("Atualização do funcionário solicitada com sucesso!"), 200