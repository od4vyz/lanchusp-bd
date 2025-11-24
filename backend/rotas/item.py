from flask import Blueprint, jsonify, request

from servicos.item import ItemDatabase

item_blueprint = Blueprint("item", __name__)

# Retorna um Item
@item_blueprint.route("/item", methods=["GET"])
def get_item():    
    # Parâmetros - Filtra por nome, lanchonete_end ou categoria
    nome = request.args.get("nome", "")
    lanchonete_end = request.args.get("lanchonete_end", "")
    categoria = request.args.get("categoria", "")
    return jsonify(ItemDatabase().get_item(nome, lanchonete_end, categoria)), 200

# Insere um Item novo
@item_blueprint.route("/item", methods=["POST"])
def insere_item():
    json = request.get_json()
    nome = json.get("nome")
    lanchonete_end = json.get("lanchonete_end")
    categoria = json.get("categoria")
    registro = ItemDatabase().regristra_item(nome, lanchonete_end, categoria)

    if not registro:
        return jsonify("Não foi possível registrar o item"), 400

    return jsonify("Item registrado com sucesso!"), 200

# Remove um Cliente
@item_blueprint.route("/item", methods=["DELETE"])
def deleta_item():
    nome = request.args.get("nome", "")
    lanchonete_end = request.args.get("lanchonete_end", "")
    categoria = request.args.get("categoria", "")
    delete = ItemDatabase().remove_item(nome, lanchonete_end, categoria)

    if not delete:
        return jsonify("Não foi possível solicitar a remoção do Item"), 400

    return jsonify("Remoção do Item solicitada com sucesso!"), 200