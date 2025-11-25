from servicos.database.conector import DatabaseManager

class ProdutoProntoDatabase():
    def __init__(self, db_provider = DatabaseManager()):
        self.db = db_provider

    # Busca por um Produto_Pronto com base no nome ou categoria
    def get_produtoPronto(self, nome: str, categoria: str):
        query = """
                SELECT * FROM Produto_Pronto pp
                """
        if nome:
            query+=f"WHERE pp.Nome_Item = '{nome}'\n"
        if categoria:
            if "WHERE" in query:
                query+=f"AND pp.Categoria= '{categoria}'\n"
            else:
                query+=f"WHERE pp.Categoria = '{categoria}'\n"

        return self.db.execute_select_all(query)
    
    # Registra uma novo Produto_Pronto
    def regristra_produtoPronto(self, nome:str, categoria:str) -> bool:
        statement = f"INSERT INTO Produto_Pronto (Nome_Item, categoria) VALUES ('{nome}', '{categoria}');\n"
        return self.db.execute_statement(statement)
    
    # Remove um Produto_Pronto com base no nome ou categoria
    def remove_produtoPronto(self, nome:str, categoria:str) -> bool:
        # Pra não deletar a tabela toda se não tiver parâmetro
        if  nome or categoria:
            statement = "DELETE FROM Produto_Pronto pp "
            if nome:
                statement+=f"WHERE pp.Nome_Item = '{nome}'\n" 
            if categoria:
                if "WHERE" in statement:
                    statement+=f"AND pp.Categoria = '{categoria}'\n"
                else:
                    statement+=f"WHERE pp.Categoria = '{categoria}'\n"
            
        return self.db.execute_statement(statement)
    
    # Atualiza um Produto_Pronto com base no nome
    def atualiza_produtoPronto(self, nome:str, nome_novo:str, categoria_nova:str) -> bool:
        statement = "UPDATE Produto_Pronto pp "
        # SET
        if nome_novo:
            statement+=f"SET Nome_Item= '{nome_novo}'\n" 
        if categoria_nova:
            if "SET" in statement:
                statement+=f", Categoria = '{categoria_nova}'\n"
            else:
                statement+=f"SET Categoria = '{categoria_nova}'\n"
        # WHERE
        if nome:
            statement+=f"WHERE pp.Nome_Item = '{nome}'\n" 
            
        return self.db.execute_statement(statement)