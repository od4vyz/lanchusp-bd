from servicos.database.conector import DatabaseManager

class FornecedorDatabase():
    def __init__(self, db_provider = DatabaseManager()):
        self.db = db_provider

    # Busca pelo fornecedor usando a localização ou o nome
    def get_fornecedor(self, localizacao: str, nome: str):
        query = """
                SELECT * FROM fornecedor f
                """
        if localizacao:
            query+=f"WHERE f.localizacao = '{localizacao}'\n"
        if nome:
            if "WHERE" in query:
                query+=f"AND f.nome = '{nome}'\n"
            else:
                query+=f"WHERE f.nome = '{nome}'\n"

        return self.db.execute_select_all(query)
    
    # Registra um fornecedor novo no Banco de Dados
    def regristra_fornecedor(self, localizacao:str, nome:str) -> bool:
        statement = f"INSERT INTO fornecedor (localizacao, nome) VALUES ('{localizacao}', '{nome}');\n"
        return self.db.execute_statement(statement)
    
    # Remove um fornecedor com base na localizacao ou nome
    def remove_fornecedor(self, localizacao:str, nome:str) -> bool:
        # Pra não deletar a tabela toda se não tiver parâmetro
        if localizacao or nome:
            statement = "DELETE FROM fornecedor f "
            if localizacao:
                statement+=f"WHERE f.localizacao = '{localizacao}'\n" 
            if nome:
                if "WHERE" in statement:
                    statement+=f"AND f.nome = '{nome}'\n"
                else:
                    statement+=f"WHERE f.nome = '{nome}'\n"

        return self.db.execute_statement(statement)