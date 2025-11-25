from flask import Blueprint, jsonify, request

from servicos.receita import ReceitaDatabase

receita_blueprint = Blueprint("receita", __name__)

# Retorna uma Receita
@receita_blueprint.route("/receita", methods=["GET"])
def get_receita():    
    # Parâmetros - Filtra por nome ou categoria da receita
    nome = request.args.get("nome", "")
    categoria = request.args.get("categoria", "")
    return jsonify(ReceitaDatabase().get_receita(nome, categoria)), 200

# Insere uma Receita nova
@receita_blueprint.route("/receita", methods=["POST"])
def insere_receita():
    json = request.get_json()
    nome = json.get("Nome_Item")
    categoria = json.get("Categoria")
    tempo_medio_preparo = json.get("Tempo_Medio_Preparo")
    registro = ReceitaDatabase().regristra_receita(nome, categoria, tempo_medio_preparo)

    if not registro:
        return jsonify("Não foi possível registrar a receita"), 400

    return jsonify("Receita registrada com sucesso!"), 200

# Remove uma receita
@receita_blueprint.route("/receita", methods=["DELETE"])
def deleta_receita():
    nome = request.args.get("nome", "")
    categoria = request.args.get("categoria", "")
    delete = ReceitaDatabase().remove_receita(nome, categoria)

    if not delete:
        return jsonify("Não foi possível solicitar a remoção da receita"), 400

    return jsonify("Remoção da receita solicitada com sucesso!"), 200

# Atualiza uma Receita
@receita_blueprint.route("/receita", methods=["PUT"])
def atualiza_receita():
    nome = request.args.get("nome", "")
    nome_novo = request.args.get("nome_novo", "")
    categoria_nova = request.args.get("categoria_nova", "")
    tempo_medio_preparo = request.args.get("tempo_medio_preparo", "")
    delete = ReceitaDatabase().atualiza_receita(nome, nome_novo, categoria_nova, tempo_medio_preparo)

    if not delete:
        return jsonify("Não foi possível solicitar a atualização da receita"), 400

    return jsonify("Atualização da receita solicitada com sucesso!"), 200