# Projeto de automação de extração de dados de sites e tratamento de base de dados com Pandas.

![Python](https://www.python.org/static/community_logos/python-logo-master-v3-TM.png)

## Descrição
Este projeto realiza a automação da extração de dados de sites utilizando Python, além de tratar e limpar a base rmazenada em um arquivo CSV com a biblioteca Pandas. Após o tratamento, 
os dados são carregados no Google BigQuery para armazenamento e análises futuras.

## Funcionalidades
- Automação de extração de dados via web scraping.
- Limpeza da colunas para remover strings desnecessárias.
- Conexão e upload dos dados processados no Google BigQuery.
- Automação com Selenium.

## Estrutura do Projeto
- `auto.py`: Contém o arquivo CSV bruto e o arquivo limpo.
- `csvread.py`: Contém o código-fonte Python para tratamento de dados e integração com BigQuery.
- `README.md`: Este arquivo de documentação.

## Como Executar
1. **Instale as Dependências**:
   ```bash
   pip install -r requirements.txt
