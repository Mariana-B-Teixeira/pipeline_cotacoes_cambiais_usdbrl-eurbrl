import os # Biblioteca nativa do Python para se comunicar com o Sistema Operacional
import requests # Biblioteca de requisições  Python para usar na API
import psycopg # Permite que o Python se comunique com o PostgreSQL
from dotenv import load_dotenv # Biblioteca externa que lê arquiv .env

load_dotenv() # Pega .env do disco e coloca na memória RAM para trabalhar com esse ambiente

def main():
    
        dados_brutos = extrair()
        if dados_brutos is None:
              print("Não foi possível obter os dados no momento.")
        else:
            dados_tratados = transformar(dados_brutos)
            carregar(dados_tratados)

def extrair():
    try:
    # Colocando o URL da API pública em uma variável.
        url = "https://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL"

    # Obtendo dados que estão na URL com uma requisição HTTP do tipo GET.       
        resposta = requests.get(url)

        resposta.raise_for_status()

        #Transforma em json.
        dados = resposta.json()
        
        print(dados)
        
        print(" ")
        
        return dados

    except requests.exceptions.ConnectionError:
            print("Erro de conexão.")
            return None
    except requests.exceptions.HTTPError:
            print("Resposta HTTP inválida")
            return None
    except requests.exceptions.Timeout:
            print("Requsição excedeu tempo limite")
            return None
    except requests.exceptions.TooManyRedirects:
            print("Número máximo de redirecionamentos excedido")
            return None

def transformar(dados):
    # Cotação de compra do dólar.
    print("------COMPRA DO DÓLAR:------")
    print(dados["USDBRL"]["bid"])
    dolar_compra = dados["USDBRL"]["bid"]
    dolar_compra = float(dolar_compra)

    print(" ")

    # Cotação de venda do dólar.
    print("------VENDA DO DÓLAR:------")
    print(dados["USDBRL"]["ask"])
    dolar_venda = dados["USDBRL"]["ask"]
    dolar_venda = float(dolar_venda)

    print(" ")

    # Data do valor:
    print("-----------DATA:-----------")

    print(dados["USDBRL"]["create_date"])
    dolar_data = dados["USDBRL"]["create_date"][0:10]

    print(" ")

    print("---------------------------")

    print(" ")

    # Cotação de compra do euro.
    print("------COMPRA DO EURO:------")
    print(dados["EURBRL"]["bid"])
    euro_compra = dados["EURBRL"]["bid"]
    euro_compra = float(euro_compra)

    print(" ")

    # Cotação de venda do euro.
    print("------VENDA DO EURO:------")
    print(dados["EURBRL"]["ask"])
    euro_venda = dados["EURBRL"]["ask"]
    euro_venda = float(euro_venda)

    print(" ")

    # Data do valor:
    print("-----------DATA:-----------")

    print(dados["EURBRL"]["create_date"])
    euro_data = dados["EURBRL"]["create_date"][0:10]

    print(" ")

    valores = [
            {"moeda": "dolar", "compra": dolar_compra, "venda": dolar_venda, "data": dolar_data},
            {"moeda": "euro", "compra": euro_compra, "venda": euro_venda, "data": euro_data}
        ]
    
    return valores
    
def carregar(valores):
    # Obtém informações de ambiente do .env
    user = os.getenv("POSTGRES_USER").strip()
    password = os.getenv("POSTGRES_PASSWORD").strip()
    dbname = os.getenv("POSTGRES_DB").strip()
    host = os.getenv("POSTGRES_HOST").strip()
    port = os.getenv("POSTGRES_PORT").strip()

    # Formato URI de conexão com o banco de dados PostgreSQL
    db_url = f"postgresql://{user}:{password}@{host}:{port}/{dbname}"

    # O 'with' na conexão gerencia a transação (commit/rollback) e fecha a conexão ao final
    # O 'with' no cursor garante que o cursor seja fechado após o bloco
    with psycopg.connect(db_url) as con:
        with con.cursor() as cur:
            cur.execute("""
                CREATE TABLE IF NOT EXISTS cambio (
                    moeda TEXT, 
                    valor_de_compra REAL, 
                    valor_de_venda REAL, 
                    data TEXT,
                    UNIQUE(moeda, data)
                )
            """)
            
            for i in valores:
                cur.execute(
                    """
                    INSERT INTO cambio (moeda, valor_de_compra, valor_de_venda, data) 
                    VALUES (%s, %s, %s, %s) 
                    ON CONFLICT (moeda, data) DO NOTHING
                    """,
                    (
                        i["moeda"],
                        i["compra"],
                        i["venda"],
                        i["data"]
                    )   
                )

        # O 'con.commit()' manual não é mais necessário aqui!
        # O 'with con' faz o commit automaticamente se não houver erros.

main()