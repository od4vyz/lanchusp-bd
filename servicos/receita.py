from servicos.database.conector import DatabaseManager

class ReceitaDatabase():
    def __init__(self, db_provider = DatabaseManager()):
        self.db = db_provider

    # Seleciona todas os itens que compôem a receita de algum item artesanal
    def get_receita(self):
        query = """
                SELECT * FROM Receita r
                """

        return self.db.execute_select_all(query)