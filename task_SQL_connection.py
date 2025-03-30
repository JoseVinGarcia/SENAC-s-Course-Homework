from sqlalchemy import create_engine, text
import os

# DB connection variables
host = "localhost"
user = "root"
password = "root"
roots = 0

# Function to connect to the database
def conecta_banco(b,c):
    try:
        # BD's connection URL using SQLAlchemy and PyMySQL
        engine = create_engine(f"mysql+pymysql://{user}:{password}@{host}/{b}")

        # Start a connection
        with engine.connect() as conexao:
            # Query: "SQL language to select all records from the products table"
            query = c

            # "text(query)" transforms the query string into an object compatible with SQLAlchemy
            # "conexao.execute" executes this query in the database.
            resultados = conexao.execute(text(query))

            for item in resultados:
                print(item[0], item[1], item[2])

    except ImportError as e:
        print(f"Erro: {e}")


# Beggining of the code
os.system("cls")
print("="*30)
print("SQL EXAMINADOR ~~ Por José Vinícius")

bd = input("\n     Digite o nome da base de dados: ")
cd = input("     Agora digite seu comando: ")

# Call the function that connects to the database
# conecta_banco(bd,cd)

while roots==0:
    conecta_banco(bd,cd)
    cmd = input("     Deseja realizar outro comando? S/N: ").upper()
    if cmd == "S":
        cd = input("     Agora digite seu comando: ")
    else:
        roots=1

print("Até mais!")
