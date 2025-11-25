from servicos.database.conector import DatabaseManager

class ReceitaDatabase():
    def __init__(self, db_provider = DatabaseManager()):
        self.db = db_provider

    # Busca por uma receita com base no nome ou categoria
    def get_receita(self, nome: str, categoria: str):
        query = """
                SELECT * FROM Receita r
                """
        if nome:
            query+=f"WHERE r.Nome_Item = '{nome}'\n"
        if categoria:
            if "WHERE" in query:
                query+=f"AND r.Categoria= '{categoria}'\n"
            else:
                query+=f"WHERE r.Categoria = '{categoria}'\n"

        return self.db.execute_select_all(query)
    
    # Registra uma nova receita
    def regristra_receita(self, nome:str, categoria:str, tempo_medio_preparo) -> bool:
        statement = f"INSERT INTO Receita (Nome_Item, categoria, Tempo_Medio_Preparo) VALUES ('{nome}', '{categoria}', {tempo_medio_preparo});\n"
        return self.db.execute_statement(statement)
    
    # Remove uma receita com base no nome ou categoria
    def remove_receita(self, nome:str, categoria:str) -> bool:
        # Pra não deletar a tabela toda se não tiver parâmetro
        if  nome or categoria:
            statement = "DELETE FROM receita r "
            if nome:
                statement+=f"WHERE r.Nome_Item = '{nome}'\n" 
            if categoria:
                if "WHERE" in statement:
                    statement+=f"AND r.Categoria = '{categoria}'\n"
                else:
                    statement+=f"WHERE r.Categoria = '{categoria}'\n"
            
        return self.db.execute_statement(statement)
    
    # Atualiza a receita com base no nome
    def atualiza_receita(self, nome:str, nome_novo:str, categoria_nova:str, tempo_medio_preparo) -> bool:
        statement = "UPDATE Receita r "
        # SET
        if nome_novo:
            statement+=f"SET Nome_Item= '{nome_novo}'\n" 
        if categoria_nova:
            if "SET" in statement:
                statement+=f", Categoria = '{categoria_nova}'\n"
            else:
                statement+=f"SET Categoria = '{categoria_nova}'\n"
        if tempo_medio_preparo:
            if "SET" in statement:
                statement+=f", Tempo_Medio_Preparo = '{tempo_medio_preparo}'\n"
            else:
                statement+=f"SET Tempo_Medio_Preparo = '{tempo_medio_preparo}'\n"
        # WHERE
        if nome:
            statement+=f"WHERE r.Nome_Item = '{nome}'\n" 
            
        return self.db.execute_statement(statement)