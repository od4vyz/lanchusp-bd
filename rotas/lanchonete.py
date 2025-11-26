from flask import Blueprint, jsonify, request, render_template

from servicos.lanchonete import LanchoneteDatabase
from servicos.catalogo import CatalogoDatabase
from servicos.dashboard import DashboardDatabase


lanchonete_blueprint = Blueprint("lanchonete", __name__)

# Renderizacao dos templates

@lanchonete_blueprint.route("/<string:campus>", methods=["GET"])
def render_dashboard(campus):

    lanchonete_dashboard = LanchoneteDatabase().get_lanchonete(campus, "")
    
    print(lanchonete_dashboard[0])
    media_valor = DashboardDatabase().get_media()
    media_valor[0]['media'] = "{:.2f}".format(media_valor[0]['media'])
    cliente_vip = DashboardDatabase().get_clientes_vip()
    analise_vendas = DashboardDatabase().get_analise_vendas_categoria(campus)
    folha_pagamento = DashboardDatabase().get_folha_de_pagamento(campus)
    for item in folha_pagamento:
        item['media_salarial'] = "{:.2f}".format(item['media_salarial'])
    eficiencia_menu = DashboardDatabase().get_eficiencia_menu()

    return render_template("dashboard.html", media=media_valor[0], clienteVip=cliente_vip, analiseVendas=analise_vendas, folhaPagamento=folha_pagamento,
                                            eficiencia=eficiencia_menu, lanchonete=lanchonete_dashboard[0])

@lanchonete_blueprint.route("/<string:campus>/estoque", methods=["GET"])
def render_estoque(campus):

    dados_estoque = CatalogoDatabase().get_estoque(campus)

    return render_template("estoque.html", estoque=dados_estoque, lanchonete={"campus": campus})

@lanchonete_blueprint.route("/<string:campus>/catalogo", methods=["GET"])
def render_catalogo(campus):

    dados_catalogo = CatalogoDatabase().get_catalogo(campus)

    return render_template("catalogo.html", catalogo=dados_catalogo, lanchonete={"campus": campus})

# # Retorna uma Lanchonete
# @lanchonete_blueprint.route("/lanchonete", methods=["GET"])
# def get_lanchonete():    
#     # Parâmetros - Filtra por localizacao e nome
#     localizacao = request.args.get("localizacao", "")
#     nome = request.args.get("nome", "")
#     return jsonify(LanchoneteDatabase().get_lanchonete(localizacao, nome)), 200

# # Insere uma Lanchonete nova
# @lanchonete_blueprint.route("/lanchonete", methods=["POST"])
# def insere_lanchonete():
#     json = request.get_json()
#     localizacao = json.get("localizacao")
#     nome = json.get("nome")
#     registro = LanchoneteDatabase().regristra_lanchonete(localizacao, nome)

#     if not registro:
#         return jsonify("Não foi possível registrar a lanchonete"), 400

#     return jsonify("Lanchonete registrada com sucesso!"), 200

# # Remove uma Lanchonete
# @lanchonete_blueprint.route("/lanchonete", methods=["DELETE"])
# def deleta_lanchonete():
#     localizacao = request.args.get("localizacao", "")
#     nome = request.args.get("nome", "")
#     delete = LanchoneteDatabase().remove_lanchonete(localizacao, nome)

#     if not delete:
#         return jsonify("Não foi possível solicitar a remoção da lanchonete"), 400

#     return jsonify("Remoção da lanchonete solicitada com sucesso!"), 200

# # Atualiza uma Lanchonete
# @lanchonete_blueprint.route("/lanchonete", methods=["PUT"])
# def atualiza_lanchonete():
#     localizacao = request.args.get("localizacao", "")
#     nome = request.args.get("nome", "")
#     localizacao_nova = request.args.get("localizacao_nova", "")
#     nome_novo = request.args.get("nome_novo", "")
#     update = LanchoneteDatabase().atualiza_lanchonete(localizacao, localizacao_nova, nome, nome_novo)

#     if not update:
#         return jsonify("Não foi possível solicitar a atualização da lanchonete"), 400

#     return jsonify("Atualização da lanchonete solicitada com sucesso!"), 200
