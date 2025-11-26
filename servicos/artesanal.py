from servicos.database.conector import DatabaseManager

class ArtesanalDatabase():
    def __init__(self, db_provider = DatabaseManager()):
        self.db = db_provider

    # Seleciona todos os itens artesanais
    def get_artesanal(self):
        query = """
                SELECT * FROM Artesanal a
                """

        return self.db.execute_select_all(query)