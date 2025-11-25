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
Na pasta backend:
```bash
python -m venv venv 
.\venv\Scripts\activate
pip install -r requirements.txt
```  
Criar uma Database no PostgreSQL com o nome "lanchusp"  
Configurar em backend\servicos\database\conector.py o usuário e senha do seu pgAdmin  

## Execução Backend
Na pasta backend:
```bash
python main.py
```
