from servicos.database.conector import DatabaseManager

class FuncionarioDatabase():
    def __init__(self, db_provider = DatabaseManager()):
        self.db = db_provider

    # Busca pelo funcionario usando o cpf ou nome
    def get_funcionario(self, cpf: str, nome: str):
        query = """
                SELECT * FROM funcionario f
                """
        if cpf:
            query+=f"WHERE f.CPF = '{cpf}'\n"
        if nome:
            if "WHERE" in query:
                query+=f"AND f.nome = '{nome}'\n"
            else:
                query+=f"WHERE f.nome = '{nome}'\n"

        return self.db.execute_select_all(query)
    
    # Busca pelos funcionarios de uma lanchonete específica
    def get_funcionarios_lanchonete(self, campus: str):
        # filtro obrigatório de lanchonete
        if campus:
            query = f"""
                    SELECT *
                    FROM Funcionario f
                    WHERE EXISTS(
                        SELECT *
                        FROM Quadro_Funcionarios qf
                        WHERE f.cpf = qf.cpf AND qf.campus = '{campus}'
                    )
                    """
        return self.db.execute_select_all(query)
    
    # Busca pelos funcionarios de uma lanchonete específica
    def get_funcionarios_coringas(self):
        # filtro obrigatório de lanchonete
        query = f"""
                SELECT *
                FROM Funcionario f1
                WHERE NOT EXISTS(
                    (
                    SELECT Campus
                    FROM Lanchonete l
                    )
                    EXCEPT
                    (
                    SELECT L.Campus
                    FROM Funcionario f2
                    JOIN Quadro_Funcionarios Q ON f2.CPF = Q.CPF 
                    JOIN Lanchonete L ON Q.Campus = L.Campus
                    WHERE f2.CPF = f1.CPF
                    )
                )
                """
        return self.db.execute_select_all(query)
    
    def get_media_salarial_cargo(self):
        query = f"""
                SELECT Cargo, 
                AVG(Salario) AS Media_Salarial, 
                COUNT(*) AS Qtd_Funcionarios
                FROM Quadro_Funcionarios
                GROUP BY Cargo
                HAVING COUNT(*) > 2;
                """
        return self.db.execute_select_all(query)

    
    # Registra um novo funcionário no Banco de Dados
    def regristra_funcionario(self, cpf:str, nome:str) -> bool:
        statement = f"INSERT INTO funcionario (CPF, nome) VALUES ('{cpf}', '{nome}');\n"
        return self.db.execute_statement(statement)
    
    # Remove um funcionário com base no cpf ou nome
    def remove_funcionario(self, cpf:str, nome:str) -> bool:
        # Pra não deletar a tabela toda se não tiver parâmetro
        if cpf or nome:
            statement = "DELETE FROM funcionario f "
            if cpf:
                statement+=f"WHERE f.CPF = '{cpf}'\n" 
            if nome:
                if "WHERE" in statement:
                    statement+=f"AND f.nome = '{nome}'\n"
                else:
                    statement+=f"WHERE f.nome = '{nome}'\n"
        return self.db.execute_statement(statement)
    
    # Atualiza um Funcionario com base no cpf ou nome
    def atualiza_funcionario(self, cpf:str, cpf_novo:str, nome:str, nome_novo:str) -> bool:
        statement = "UPDATE Funcionario f "
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
            statement+=f"WHERE f.CPF = '{cpf}'\n" 
        if nome:
            if "WHERE" in statement:
                statement+=f"AND f.nome = '{nome}'\n"
            else:
                statement+=f"WHERE f.nome = '{nome}'\n"
            
        return self.db.execute_statement(statement)