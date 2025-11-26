from servicos.database.conector import DatabaseManager

class ClienteDatabase():
    def __init__(self, db_provider = DatabaseManager()):
        self.db = db_provider

    # Seleciona todos os clientes
    def get_cliente(self, cpf: str, nome: str, id):
        query = """
                SELECT * FROM cliente c
                """
        if cpf:
            query+=f"WHERE c.CPF = '{cpf}'\n"
        if nome:
            if "WHERE" in query:
                query+=f"AND c.nome = '{nome}'\n"
            else:
                query+=f"WHERE c.nome = '{nome}'\n"
        if id:
            if "WHERE" in query:
                query+=f"AND c.id = {id}\n"
            else:
                query+=f"WHERE c.id = {id}\n"

        return self.db.execute_select_all(query)
    
    # Registra um novo cliente no Banco de Dados
    def regristra_cliente(self, cpf:str, nome:str) -> bool:
        statement = f"INSERT INTO cliente (CPF, nome) VALUES ('{cpf}', '{nome}');\n"
        return self.db.execute_statement(statement)
    
    # Remove um cliente com base no cpf, nome ou número do cliente
    def remove_cliente(self, cpf:str, nome:str, id) -> bool:
        # Pra não deletar a tabela toda se não tiver parâmetro
        if cpf or nome or id:
            statement = "DELETE FROM cliente c "
            if cpf:
                statement+=f"WHERE c.CPF = '{cpf}'\n" 
            if nome:
                if "WHERE" in statement:
                    statement+=f"AND c.nome = '{nome}'\n"
                else:
                    statement+=f"WHERE c.nome = '{nome}'\n"
            if id:
                if "WHERE" in statement:
                    statement+=f"AND c.id = {id}\n"
                else:
                    statement+=f"WHERE c.id = {id}\n"
        return self.db.execute_statement(statement)
    
    # Atualiza um cliente com base no cpf, nome ou número do cliente
    def atualiza_cliente(self, cpf:str, cpf_novo:str, nome:str, nome_novo:str, id) -> bool:
        statement = "UPDATE Cliente c "
        # SET
        if cpf_novo:
            statement+=f"SET CPF= '{cpf_novo}'\n" 
        if nome_novo:
            if "SET" in statement:
                statement+=f", nome = '{nome_novo}'\n"
            else:
                statement+=f"SET nome = '{nome_novo}'\n"
        # WHERE
        if cpf:
            statement+=f"WHERE c.CPF = '{cpf}'\n" 
        if nome:
            if "WHERE" in statement:
                statement+=f"AND c.nome = '{nome}'\n"
            else:
                statement+=f"WHERE c.nome = '{nome}'\n"
        if id:
            if "WHERE" in statement:
                statement+=f"AND c.id = {id}\n"
            else:
                statement+=f"WHERE c.id = {id}\n"
            
        return self.db.execute_statement(statement)