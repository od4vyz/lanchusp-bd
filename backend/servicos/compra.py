from servicos.database.conector import DatabaseManager

class CompraDatabase():
    def __init__(self, db_provider = DatabaseManager()):
        self.db = db_provider

    # Seleciona todas as compras feitas por todas as lanchonetes
    def get_compra(self):
        query = """
                SELECT * FROM Compra c
                """

        return self.db.execute_select_all(query)