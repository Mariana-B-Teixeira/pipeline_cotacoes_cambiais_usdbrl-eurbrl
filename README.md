# 💱 Pipeline de Cotações Cambiais (USD/BRL - EUR/BRL)
 
![Python](https://img.shields.io/badge/Python-3-blue?logo=python&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-database-lightgrey?logo=sqlite)
![Status](https://img.shields.io/badge/status-em%20evolução-yellow)
 
Pipeline **ETL** em Python que busca cotações de câmbio (Dólar e Euro em relação ao Real) através de uma API pública, trata os dados e os persiste em um banco de dados.
 
> 🎯 Este projeto foi construído para fortalecer meus estudos em Python, SQL e Engenharia de Pipelines de Dados, aplicando na prática conceitos de ETL (Extract, Transform, Load), tratamento de erros e organização de código.
>
> ✨ Além disso, utilizarei este mesmo script como base para implementar ferramentas como PostgreSQL, Docker e Apache Airflow. O foco principal não é a complexidade das regras de negócio, mas sim a construção de uma arquitetura de dados moderna, escalável e produtiva (Production-Ready Architecture) utilizando as principais tecnologias do mercado.

---
 
## ⚙️ O que o projeto faz
 
| Etapa | Descrição |
|---|---|
| 📥 **Extrai** | Busca as cotações de compra e venda do Dólar e do Euro na [AwesomeAPI](https://docs.awesomeapi.com.br/api-de-moedas) |
| 🔄 **Transforma** | Converte os valores de string para número (`float`) e normaliza a data (`AAAA-MM-DD`) |
| 💾 **Carrega** | Persiste os dados em SQLite (`cambio.db`), evitando duplicar a mesma moeda no mesmo dia |
 
---
 
## 🗺️ Roadmap
 
- [x] Extração de dados via API pública
- [x] Tratamento de erros de conexão/HTTP
- [x] Transformação dos dados (tipos e formato de data)
- [x] Persistência em SQLite com controle de duplicatas
- [x] Código organizado em funções desacopladas (`extrair`, `transformar`, `carregar`)
- [ ] 🐘 Migração para PostgreSQL
- [ ] 🐳 Containerização com Docker
- [ ] 🔗 Orquestração com Airflow
---
 
## 🛠️ Tecnologias
 
- **Python 3**
- [`requests`](https://requests.readthedocs.io/) — requisições HTTP
- `sqlite3` — banco de dados
---
 
## 🚀 Como rodar
 
```bash
pip install requests
python main.py
```
 
O script grava as cotações do dia em `cambio.db`, na mesma pasta, ignorando automaticamente registros repetidos da mesma moeda no mesmo dia.
 
---
 
## 🗃️ Estrutura da tabela `cambio`
 
| Coluna | Tipo | Descrição |
|---|---|---|
| `moeda` | TEXT | Nome da moeda (`dolar` ou `euro`) |
| `valor_de_compra` | REAL | Cotação de compra |
| `valor_de_venda` | REAL | Cotação de venda |
| `data` | TEXT | Data da cotação (`AAAA-MM-DD`) |
 
🔒 Uma constraint `UNIQUE(moeda, data)` garante que não haja registros duplicados.
 
---
 
## 🔍 Visualizando os dados
 
O arquivo `cambio.db` pode ser inspecionado com qualquer cliente SQLite, como o [DBeaver](https://dbeaver.io/) — basta conectar como um banco SQLite e apontar para o arquivo gerado.
 
---
 
## 🌐 Fonte dos dados
 
[AwesomeAPI](https://docs.awesomeapi.com.br/api-de-moedas) — API pública e gratuita de cotações.

---

⭐ Desenvolvido por **Mariana B. Teixeira**

 
