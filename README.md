# 💱 Pipeline de Cotações Cambiais (USD/BRL - EUR/BRL)

![Python](https://img.shields.io/badge/Python-3-blue?logo=python&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-database-blue?logo=postgresql)
![Status](https://img.shields.io/badge/status-em%20evolução-yellow)

Pipeline **ETL** em Python que busca cotações de câmbio (Dólar e Euro em relação ao Real) através de uma API pública, trata os dados e os persiste em um banco de dados relacional.

> 🎯 Este projeto foi construído para fortalecer meus estudos em **Python, SQL e engenharia de pipelines de dados**, aplicando na prática conceitos de ETL (*Extract, Transform, Load*), tratamento de erros, variáveis de ambiente e organização de código.

---

## ⚙️ O que o projeto faz

| Etapa | Descrição |
|---|---|
| 📥 **Extrai** | Busca as cotações de compra e venda do Dólar e do Euro na [AwesomeAPI](https://docs.awesomeapi.com.br/api-de-moedas) |
| 🔄 **Transforma** | Converte os valores de string para número (`float`) e normaliza a data (`AAAA-MM-DD`) |
| 💾 **Carrega** | Persiste os dados no **PostgreSQL**, evitando duplicar a mesma moeda no mesmo dia |

---

## 🗺️ Roadmap

- [x] Extração de dados via API pública
- [x] Tratamento de erros de conexão/HTTP
- [x] Transformação dos dados (tipos e formato de data)
- [x] Código organizado em funções desacopladas (`extrair`, `transformar`, `carregar`)
- [x] 🐘 Migração para PostgreSQL com gerenciamento de variáveis de ambiente (`.env`)
- [ ] 🐳 Containerização com Docker
- [ ] 🔗 Orquestração com Airflow

---

## 🛠️ Tecnologias

- **Python 3**
- [`requests`](https://requests.readthedocs.io/) — requisições HTTP
- [`psycopg`](https://www.psycopg.org/psycopg3/docs/) — driver nativo para PostgreSQL
- [`python-dotenv`](https://pypi.org/project/python-dotenv/) — gerenciamento de variáveis de ambiente
- **PostgreSQL** — banco de dados relacional

---

## 🚀 Como rodar

### 1. Instalar dependências
```bash
pip install requests psycopg "psycopg[binary]" python-dotenv
````
---

⭐ Desenvolvido por **Mariana B. Teixeira**
