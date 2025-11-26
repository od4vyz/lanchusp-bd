from servicos.database.conector import DatabaseManager

class Quadro_FuncionariosDatabase():
    def __init__(self, db_provider = DatabaseManager()):
        self.db = db_provider

    # Seleciona o quadro de todos os funcionários
    def get_quadro_funcionarios(self, campus: str, cpf: str):
        query = """
                SELECT * FROM Funcionario f
                    JOIN Quadro_Funcionarios qf ON f.CPF = qf.CPF
                """
        if campus:
            query+=f"WHERE qf.campus = '{campus}'\n"
        if cpf:
            if "WHERE" in query:
                query+=f"AND qf.cpf = '{cpf}'\n"
            else:
                query+=f"WHERE qf.cpf = '{cpf}'\n"

        return self.db.execute_select_all(query)