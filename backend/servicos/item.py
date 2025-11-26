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
    
    # Retorna itens parados no estoque (não vendidos nos últimos 30 dias)
    def get_itens_estoque(self, campus: str):
        query = f"""
                SELECT C.NomeItem
                FROM Catalogo C
                WHERE C.Campus = '{campus}'
                AND NOT EXISTS (
                    SELECT 1
                    FROM Pedido_Item PI
                    WHERE PI.NomeItem = C.NomeItem
                    AND PI.Campus = C.Campus
                );
                """
        return self.db.execute_select_all(query)

    # Retorna itens de sucesso que devem ser reabastecidos (estoque abaixo de 10 unidades)
    def get_itens_sucesso_faltantes(self):
        query = """
                SELECT C.NomeItem, C.Campus
                FROM Catalogo C
                JOIN Pedido_Item PI ON C.NomeItem = PI.NomeItem AND C.Campus = PI.Campus
                WHERE C.qtdDisponivel = 0
                GROUP BY C.NomeItem, C.Campus
                HAVING SUM(PI.Quantidade) > 10;
                """
        return self.db.execute_select_all(query)
    
    # Retorna quantidade de opções de itens disponíveis por categoria em cada lanchonete
    def get_qtd_itens_categoria(self):
        query = """
                SELECT PI.Campus, I.Categoria,
                COUNT(DISTINCT C.NomeItem) AS Variedade_Itens_No_Cardapio,
                SUM(PI.Quantidade * C.Preco) AS Faturamento_Total_Historico
                FROM Item I
                JOIN Catalogo C ON I.Nome = C.NomeItem
                LEFT JOIN Pedido_Item PI ON C.NomeItem = PI.NomeItem AND C.Campus = PI.Campus
                GROUP BY PI.Campus, I.Categoria
                ORDER BY Faturamento_Total_Historico DESC;
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