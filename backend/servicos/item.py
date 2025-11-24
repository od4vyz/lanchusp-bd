from servicos.database.conector import DatabaseManager

class ItemDatabase():
    def __init__(self, db_provider = DatabaseManager()):
        self.db = db_provider

    # Busca pelo Item usando o nome, lanchonete_end ou categoria
    def get_item(self, nome: str, lanchonete_end: str, categoria: str):
        query = """
                SELECT * FROM item i
                """
        if nome:
            query+=f"WHERE i.nome = '{nome}'\n"
        if lanchonete_end:
            if "WHERE" in query:
                query+=f"AND i.lanchonete_end = '{lanchonete_end}'\n"
            else:
                query+=f"WHERE i.lanchonete_end = '{lanchonete_end}'\n"
        if categoria:
            if "WHERE" in query:
                query+=f"AND i.categoria = '{categoria}'\n"
            else:
                query+=f"WHERE i.categoria = '{categoria}'\n"

        return self.db.execute_select_all(query)
    
    # Registra um novo Item no Banco de Dados
    def regristra_item(self, nome:str, lanchonete_end:str, categoria:str) -> bool:
        statement = f"INSERT INTO item (nome, lanchonete_end, categoria) VALUES ('{nome}', '{lanchonete_end}', '{categoria}');\n"
        return self.db.execute_statement(statement)
    
    # Remove um Item com base no nome, lanchonete_end ou categoria
    def remove_item(self, nome:str, lanchonete_end:str, categoria:str) -> bool:
        # Pra não deletar a tabela toda se não tiver parâmetro
        if nome or lanchonete_end or categoria:
            statement = "DELETE FROM item i "
            if nome:
                statement+=f"WHERE i.nome = '{nome}'\n" 
            if lanchonete_end:
                if "WHERE" in statement:
                    statement+=f"AND i.lanchonete_end = '{lanchonete_end}'\n"
                else:
                    statement+=f"WHERE i.lanchonete_end = '{lanchonete_end}'\n"
            if categoria:
                if "WHERE" in statement:
                    statement+=f"AND i.categoria = '{categoria}'\n"
                else:
                    statement+=f"WHERE i.categoria = '{categoria}'\n"
        return self.db.execute_statement(statement)