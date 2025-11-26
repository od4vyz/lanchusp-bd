from servicos.database.conector import DatabaseManager

class CatalogoDatabase():
    def __init__(self, db_provider = DatabaseManager()):
        self.db = db_provider

    # Seleciona todos os itens do catálogo de todos os campus
    def get_catalogo(self):
        query = """
                SELECT * FROM catalogo c
                """

        return self.db.execute_select_all(query)
    