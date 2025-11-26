from servicos.database.conector import DatabaseManager

class Compra_ItemDatabase():
    def __init__(self, db_provider = DatabaseManager()):
        self.db = db_provider

    # Seleciona todas os itens de todos os pedidos de todas as lanchonetes
    def get_pedido_item(self):
        query = """
                SELECT * FROM Pedido_Item pi
                """

        return self.db.execute_select_all(query)