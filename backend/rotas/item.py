from flask import Blueprint, jsonify, request

from servicos.item import ItemDatabase

item_blueprint = Blueprint("item", __name__)

# Retorna um Item
@item_blueprint.route("/item", methods=["GET"])
def get_item():    
    # Parâmetros - Filtra por nome, lanchonete_end ou categoria
    nome = request.args.get("nome", "")
    return jsonify(ItemDatabase().get_item(nome)), 200

# Retorna a diferença de preços de itens vendidos entre lanchonetes
@item_blueprint.route("/diferenca_precos_item", methods=["GET"])
def get_diferenca_precos_item():    
    return jsonify(ItemDatabase().get_diferenca_precos_item()), 200

# Retorna itens parados no estoque
@item_blueprint.route("/itens_parados", methods=["GET"])
def get_itens_estoque():    
    campus = request.args.get("campus", "")
    return jsonify(ItemDatabase().get_itens_estoque(campus)), 200

# Retorna a análise de vendas de produtos por categoria
@item_blueprint.route("/analise_vendas_categoria", methods=["GET"])
def get_analise_vendas_categoria():    
    return jsonify(ItemDatabase().get_analise_vendas_categoria()), 200

#  Retorna itens de sucesso que devem ser reabastecidos (estoque abaixo de 10 unidades)
@item_blueprint.route("/itens_sucesso_faltantes", methods=["GET"])
def get_itens_sucesso_faltantes():
    return jsonify(ItemDatabase().get_itens_sucesso_faltantes()), 200

# Retorna quantidade de opções de itens disponíveis por categoria em cada lanchonete
@item_blueprint.route("/qtd_itens_categoria", methods=["GET"])
def get_qtd_itens_categoria():
    return jsonify(ItemDatabase().get_qtd_itens_categoria()), 200

# Insere um Item novo
@item_blueprint.route("/item", methods=["POST"])
def insere_item():
    json = request.get_json()
    nome = json.get("nome")
    registro = ItemDatabase().regristra_item(nome)

    if not registro:
        return jsonify("Não foi possível registrar o item"), 400

    return jsonify("Item registrado com sucesso!"), 200

# Remove um Item
@item_blueprint.route("/item", methods=["DELETE"])
def deleta_item():
    nome = request.args.get("nome", "")
    delete = ItemDatabase().remove_item(nome)

    if not delete:
        return jsonify("Não foi possível solicitar a remoção do Item"), 400

    return jsonify("Remoção do Item solicitada com sucesso!"), 200

# Atualiza um Item
@item_blueprint.route("/item", methods=["PUT"])
def atualiza_item():
    nome = request.args.get("nome", "")
    nome_novo = request.args.get("nome_novo", "")
    update = ItemDatabase().atualiza_item(nome, nome_novo)

    if not update:
        return jsonify("Não foi possível solicitar a atualização do item"), 400

    return jsonify("Atualização do item solicitada com sucesso!"), 200