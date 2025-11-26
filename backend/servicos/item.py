from servicos.database.conector import DatabaseManager

class ItemDatabase():
    def __init__(self, db_provider = DatabaseManager()):
        self.db = db_provider

    # Busca pelo Item usando o nome
    def get_item(self, nome: str):
        query = """
                SELECT * FROM item i
                """
        if nome:
            query+=f"WHERE i.nome = '{nome}'\n"

        return self.db.execute_select_all(query)

    # Busca a diferença entre o maior e menor preço entre itens vendidos entre lanchonetes diferentes
    def get_diferenca_precos_item(self):
        query = """
                SELECT NomeItem, (MAX(Preco) - MIN(Preco)) AS Diferenca, MIN(Preco) AS Menor_Preco, MAX(Preco) AS Maior_Preco
                FROM Catalogo
                GROUP BY NomeItem
                HAVING MIN(Preco) <> MAX(Preco);
                """
        return self.db.execute_select_all(query)
    
    # Retorna a análise de vendas de produtos por categoria
    def get_analise_vendas_categoria(self):
        query = """
                SELECT I.Categoria, SUM(PI.Quantidade) AS Qtd_Total_Vendida, SUM(PI.Quantidade * C.Preco) AS Valor_Total_Arrecadado
                FROM Item I
                JOIN Pedido_Item PI ON I.Nome = PI.NomeItem
                JOIN Catalogo C ON PI.NomeItem = C.NomeItem AND PI.Campus = C.Campus
                GROUP BY I.Categoria
                ORDER BY Valor_Total_Arrecadado DESC;
                """
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