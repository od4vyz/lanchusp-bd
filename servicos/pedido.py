from servicos.database.conector import DatabaseManager

class PedidoDatabase():
    def __init__(self, db_provider = DatabaseManager()):
        self.db = db_provider

    # Seleciona todos os pedidos de todas as lanchonetes
    def get_pedido(self):
        query = """
                SELECT * FROM Pedido p
                """

        return self.db.execute_select_all(query)