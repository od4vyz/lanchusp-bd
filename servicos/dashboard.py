from servicos.database.conector import DatabaseManager

class DashboardDatabase():
    def __init__(self, db_provider = DatabaseManager()):
        self.db = db_provider

    
    # Retorna a media de gastos dos clientes
    def get_media(self):
        query = """
                SELECT AVG(TotalGasto) AS Media FROM 
                (
                SELECT SUM(Valor) AS TotalGasto
                FROM Pedido
                GROUP BY CPF
                )
                """
        return self.db.execute_select_all(query)

    # Retorna os clientes VIP (total gasto > media)
    def get_clientes_vip(self):
        query = """
                SELECT C.Nome, C.CPF, SUM(P.Valor) AS Total_Gasto
                FROM Cliente C
                JOIN Pedido P ON C.CPF = P.CPF
                GROUP BY C.Nome, C.CPF
                HAVING SUM(P.Valor) > (
                    SELECT AVG(TotalGasto) AS Media
                    FROM (
                        SELECT SUM(Valor) AS TotalGasto
                        FROM Pedido
                        GROUP BY CPF
                    ) AS Medias
                )
                ORDER BY Total_Gasto DESC
                """
        return self.db.execute_select_all(query)
    
    # Retorna a análise de vendas de produtos por categoria
    def get_analise_vendas_categoria(self, campus:str):
        query = """
                SELECT I.Categoria, SUM(PI.Quantidade) AS Qtd_Total_Vendida, SUM(PI.Quantidade * C.Preco) AS Valor_Total_Arrecadado
                FROM Item I
                JOIN Pedido_Item PI ON I.Nome = PI.NomeItem
                JOIN Catalogo C ON PI.NomeItem = C.NomeItem AND PI.Campus = C.Campus
				"""
        #query+=f"WHERE c.Campus = '{campus}'\n"
        query+= """
                GROUP BY I.Categoria
                ORDER BY Valor_Total_Arrecadado DESC;
                """
        return self.db.execute_select_all(query)
    
    # Retorna a folha de pagamento
    def get_folha_de_pagamento(self, campus:str):
        query = """
                SELECT Cargo,
                AVG(Salario) AS Media_Salarial,
                COUNT(*) AS Qtd_Funcionarios
                FROM Quadro_Funcionarios
                """
        #query+=f"WHERE Campus = '{campus}'\n"
        query+="GROUP BY Cargo"
        return self.db.execute_select_all(query)
    
    # Eficiencia do menu
    def get_eficiencia_menu(self):
        query = """
                SELECT I.Categoria,
                COUNT(DISTINCT C.NomeItem) AS
                Variedade_Itens_No_Cardapio,
                SUM(PI.Quantidade * C.Preco) AS
                Faturamento_Total_Historico
                FROM Item I
                JOIN Catalogo C ON I.Nome = C.NomeItem
                LEFT JOIN Pedido_Item PI ON C.NomeItem = PI.NomeItem AND
                C.Campus = PI.Campus
                GROUP BY I.Categoria
                ORDER BY Faturamento_Total_Historico DESC;
                """
        return self.db.execute_select_all(query)