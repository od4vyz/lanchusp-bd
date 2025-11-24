from servicos.database.conector import DatabaseManager

class LanchoneteDatabase():
    def __init__(self, db_provider = DatabaseManager()):
        self.db = db_provider

    # Busca pela lanchonete usando a localização ou o nome
    def get_lanchonete(self, localizacao: str, nome: str):
        query = """
                SELECT * FROM lanchonete l
                """
        if localizacao:
            query+=f"WHERE l.localizacao = '{localizacao}'\n"
        if nome:
            if "WHERE" in query:
                query+=f"AND l.nome = '{nome}'\n"
            else:
                query+=f"WHERE l.nome = '{nome}'\n"

        return self.db.execute_select_all(query)
    
    # Registra uma lanchonete nova no Banco de Dados
    def regristra_lanchonete(self, localizacao:str, nome:str) -> bool:
        statement = f"INSERT INTO lanchonete (localizacao, nome) VALUES ('{localizacao}', '{nome}');\n"
        return self.db.execute_statement(statement)
    
    # Remove uma lanchonete com base na localizacao ou nome
    def remove_lanchonete(self, localizacao:str, nome:str) -> bool:
        # Pra não deletar a tabela toda se não tiver parâmetro
        if localizacao or nome:
            statement = "DELETE FROM lanchonete l "
            if localizacao:
                statement+=f"WHERE l.localizacao = '{localizacao}'\n" 
            if nome:
                if "WHERE" in statement:
                    statement+=f"AND l.nome = '{nome}'\n"
                else:
                    statement+=f"WHERE l.nome = '{nome}'\n"

        return self.db.execute_statement(statement)