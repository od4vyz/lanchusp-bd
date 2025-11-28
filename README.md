# Lanchusp-BD
Projeto desenvolvido para a disciplina de Banco de Dados I do curso de Sistemas de Informação, ministrado na EACH-USP.

Link do DEER: https://miro.com/app/board/uXjVJlDhlWo=/?share_link_id=365894512863

Requisitos:
- PostgreSQL 18: https://www.postgresql.org/download/  
- Python 13.3.9: https://www.python.org/downloads/release/python-3139/
  - Adicionar o Python nas variáveis de ambiente
- Microsoft Build Tools: https://visualstudio.microsoft.com/pt-br/visual-cpp-build-tools/
  - Desktop development with C++

## Configuração do Ambiente
Na pasta do projeto:
```bash
python -m venv venv 
.\venv\Scripts\activate
pip install -r requirements.txt
```  
Criar uma Database no PostgreSQL com o nome "lanchusp" usando o script de "create table.txt"  
Popular o banco de dados com os inserts do arquivo "inserts.txt"  
Adicionar no arquivo \servicos\database\conector.py o usuário e senha do seu pgAdmin  

## Execução do Projeto
Na pasta do projeto:
```bash
python main.py
```
Abrir no navegador o endereço: http://127.0.0.1:8000/
