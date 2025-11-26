from flask import Blueprint, jsonify, request

from servicos.lanchonete import LanchoneteDatabase

lanchonete_blueprint = Blueprint("lanchonete", __name__)

# Retorna uma Lanchonete
@lanchonete_blueprint.route("/lanchonete", methods=["GET"])
def get_lanchonete():    
    # Parâmetros - Filtra por localizacao e nome
    localizacao = request.args.get("localizacao", "")
    nome = request.args.get("nome", "")
    return jsonify(LanchoneteDatabase().get_lanchonete(localizacao, nome)), 200

@lanchonete_blueprint.route("/lanchonetes_funcionario", methods=["GET"])
def get_lanchonetes_funcionario():    
    # Parâmetros - Filtra por funcionário
    cpf = request.args.get("cpf", "")
    nome = request.args.get("nome", "")
    return jsonify(LanchoneteDatabase().get_lanchonetes_funcionario(cpf, nome)), 200


# Insere uma Lanchonete nova
@lanchonete_blueprint.route("/lanchonete", methods=["POST"])
def insere_lanchonete():
    json = request.get_json()
    localizacao = json.get("localizacao")
    nome = json.get("nome")
    registro = LanchoneteDatabase().regristra_lanchonete(localizacao, nome)

    if not registro:
        return jsonify("Não foi possível registrar a lanchonete"), 400

    return jsonify("Lanchonete registrada com sucesso!"), 200

# Remove uma Lanchonete
@lanchonete_blueprint.route("/lanchonete", methods=["DELETE"])
def deleta_lanchonete():
    localizacao = request.args.get("localizacao", "")
    nome = request.args.get("nome", "")
    delete = LanchoneteDatabase().remove_lanchonete(localizacao, nome)

    if not delete:
        return jsonify("Não foi possível solicitar a remoção da lanchonete"), 400

    return jsonify("Remoção da lanchonete solicitada com sucesso!"), 200

# Atualiza uma Lanchonete
@lanchonete_blueprint.route("/lanchonete", methods=["PUT"])
def atualiza_lanchonete():
    localizacao = request.args.get("localizacao", "")
    nome = request.args.get("nome", "")
    localizacao_nova = request.args.get("localizacao_nova", "")
    nome_novo = request.args.get("nome_novo", "")
    update = LanchoneteDatabase().atualiza_lanchonete(localizacao, localizacao_nova, nome, nome_novo)

    if not update:
        return jsonify("Não foi possível solicitar a atualização da lanchonete"), 400

    return jsonify("Atualização da lanchonete solicitada com sucesso!"), 200