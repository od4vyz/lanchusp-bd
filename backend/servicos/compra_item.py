from servicos.database.conector import DatabaseManager

class Compra_ItemDatabase():
    def __init__(self, db_provider = DatabaseManager()):
        self.db = db_provider

    # Seleciona todos os itens presentes em todas as compras de todas as lanchoentes
    def get_compra_item(self):
        query = """
                SELECT * FROM Compra_Item ci
                """

        return self.db.execute_select_all(query)