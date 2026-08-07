# 💱 Pipeline de Cotações Cambiais (USD/BRL - EUR/BRL)

Pipeline ETL em Python que busca cotações de câmbio (Dólar e Euro em comparação ao Real) por meio de uma API pública, trata os dados e os persiste em um banco de dados relacional.

🎯 Este projeto foi construído para fortalecer meus estudos em **Python**, **SQL** e **engenharia de pipelines de dados**, aplicando na prática conceitos de ETL (Extract, Transform, Load), tratamento de erros, variáveis de ambiente, containerização e organização de código.

## ⚙️ O que o projeto faz

| Etapa | Descrição |
|---|---|
| 📥 **Extrai** | Busca as cotações de compra e venda do Dólar e do Euro na **AwesomeAPI** |
| 🔄 **Transforma** | Converte os valores de string para número (float) e normaliza a data (AAAA-MM-DD) |
| 💾 **Carrega** | Persiste os dados no **PostgreSQL**, evitando duplicar a mesma moeda no mesmo dia |

## 🗺️ Roadmap

- [x] Extração de dados via API pública
- [x] Tratamento de erros de conexão/HTTP
- [x] Transformação dos dados (tipos e formato de data)
- [x] Código organizado em funções desacopladas (extrair, transformar, carregar)
- [x] 🐘 Migração para PostgreSQL com gerenciamento de variáveis de ambiente (.env)
- [x] 🐳 Containerização e orquestração com Docker Compose
- [ ] 🔗 Orquestração com Airflow

## 🛠️ Tecnologias

* **Python 3**
* **requests** — requisições HTTP
* **psycopg** — driver nativo para PostgreSQL
* **python-dotenv** — gerenciamento de variáveis de ambiente
* **PostgreSQL** — banco de dados relacional
* **Docker & Docker Compose** — containerização e orquestração dos serviços

## ⚙️ Como rodar via Docker Compose 🐳

Com o **Docker Compose**, o ambiente sobe o banco de dados e executa a aplicação Python com integridade de serviço de forma totalmente automatizada.

### 📋 Pré-requisitos

* **Docker Desktop** instalado e em execução.
* Arquivo de variáveis de ambiente `.env` criado na raiz do projeto (baseado no `.env.example`).

---

### 1️⃣ Configuração das Variáveis de Ambiente (`.env`)

Crie um arquivo `.env` na raiz do seu projeto (copiando a estrutura do `.env.example`) e defina as credenciais para o banco de dados:

```env
POSTGRES_USER=seu_usuario_aqui
POSTGRES_PASSWORD=sua_senha_aqui
POSTGRES_DB=postgres
POSTGRES_HOST=postgres
POSTGRES_PORT=5432
```

---

### 2️⃣ Execução do Projeto

Para construir as imagens e iniciar o banco PostgreSQL e o container Python:

```bash
docker compose up --build
```

O Python somente tenta rodar depois que o banco de dados estiver 100% pronto para receber conexões.

---

### 3️⃣ Encerrar a Execução

Para parar a execução dos containers mantendo os dados do banco salvos no volume:

```bash
docker compose down
```

Caso queira interromper a execução e remover o volume de dados persistidos do PostgreSQL:

```bash
docker compose down -v
```

---

⭐ Desenvolvido por **Mariana B. Teixeira**
