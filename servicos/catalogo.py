from servicos.database.conector import DatabaseManager

class CatalogoDatabase():
    def __init__(self, db_provider = DatabaseManager()):
        self.db = db_provider

    
    # Seleciona todos os itens do catálogo
    def get_catalogo(self, campus: str):
        query = """
                SELECT campus, nomeitem, preco FROM catalogo c
                """
        query+=f"WHERE c.campus = '{campus}'"

        return self.db.execute_select_all(query)
    
    # Seleciona todos os itens do estoque
    def get_estoque(self, campus: str):
        query = """
                SELECT c.nomeitem, i.categoria, c.qtdDisponivel
                    FROM Catalogo c
                    JOIN Item i ON c.nomeitem = i.nome
                    JOIN Lanchonete l ON c.campus = l.campus
                    """
        query+=f"WHERE c.campus = '{campus}'"
        query+="""
                    ORDER BY c.qtdDisponivel ASC
                """


        return self.db.execute_select_all(query)
    