from servicos.database.conector import DatabaseManager

class ItemDatabase():
    def __init__(self, db_provider = DatabaseManager()):
        self.db = db_provider

    # Seleciona todos os itens
    def get_item(self, nome: str, categoria:str):
        query = """
                SELECT * FROM item i
                """
        if nome:
            query+=f"WHERE i.nome = '{nome}'\n"
        if categoria:
            if "WHERE" in query:
                query+=f"AND i.Categoria = '{categoria}'\n"
            else:
                query+=f"WHERE i.Categoria = '{categoria}'\n"

        return self.db.execute_select_all(query)
    
    # Registra um novo Item no Banco de Dados
    def regristra_item(self, nome:str) -> bool:
        statement = f"INSERT INTO item(nome) VALUES ('{nome}');\n"
        return self.db.execute_statement(statement)
    
    # Remove um Item com base no nome
    def remove_item(self, nome:str) -> bool:
        # Pra não deletar a tabela toda se não tiver parâmetro
        if nome:
            statement = "DELETE FROM item i "
            if nome:
                statement+=f"WHERE i.nome = '{nome}'\n" 

        return self.db.execute_statement(statement)
    
    # Atualiza um item com base no nome
    def atualiza_item(self, nome:str, nome_novo:str) -> bool:
        statement = "UPDATE Item i "
        # SET
        if nome_novo:
            statement+=f"SET nome= '{nome_novo}'\n" 
        # WHERE
        if nome:
            statement+=f"WHERE i.nome = '{nome}'\n" 
            
        return self.db.execute_statement(statement)