from typing import Any
import psycopg2
from psycopg2.extras import DictCursor

# Classe de Gerenciamento do database
class DatabaseManager:
    
    def __init__(self) -> None:
        self.conn = psycopg2.connect(
            dbname="lanchusp", # Colocar aqui o nome da Database criada no pgAdmin
            user="postgres",   # Colocar aqui o usuário do seu pgAdmin
            password="senha",  # Colocar aqui a senha do seu pgAdmin
            host="127.0.0.1",
            port=5432,
        )
        # Formato dos retornos: Dicionário do Python (Equivalente a Objetos)
        self.cursor = self.conn.cursor(cursor_factory=DictCursor)

    # Usado para Inserções, Deleções, Alter Tables
    def execute_statement(self, statement: str) -> bool:
        try:
            self.cursor.execute(statement)
            self.conn.commit()
        except:
            self.conn.reset()
            return False
        return True

    # Usado para SELECTS no geral
    def execute_select_all(self, query: str) -> list[dict[str, Any]]:
        self.cursor.execute(query)
        return [dict(item) for item in self.cursor.fetchall()]

    # Usado para SELECT com apenas uma linha de resposta
    def execute_select_one(self, query: str) -> dict | None:
        self.cursor.execute(query)
        query_result = self.cursor.fetchone()

        if not query_result:
            return None

        return dict(query_result)