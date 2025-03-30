import pandas as pd

# Let's read the file inside the Try Except to avoid mistakes :)
try:
    dados = pd.read_excel("vendas_roupas.xlsx")

    # Show the first 10 elements
    print("="*90)
    print("DADOS DO DATAFRAME:")
    print(dados.head(10))

    # Calculating and displaying the sum
    print("\nUNIDADES VENDIDAS NO TOTAL:")
    print(dados["Unidades Vendidas"].sum())

    # Calculating and displaying the average
    print("\nMÉDIA DE PREÇO POR UNIDADE:")
    print(dados["Preço por Unidade (R$)"].mean())

    #Calculating the highest total revenue among products:
    
    # 1. Defining the highest revenue value
    fattotal = dados["Faturamento Total (R$)"].max()
    
    # 2. Creating a dataframe filtering by the value created above
    dffatt = dados[dados["Faturamento Total (R$)"] == fattotal]

    # 3. Exibiting
    print("\nPRODUTO COM MAIOR FATURAMENTO:")
    print(dffatt[["Produto", "Faturamento Total (R$)"]])

    # calculating the lowest total revenue among products:
    # Realizing the same steps we did to display the highest revenue!
    fattmin = dados["Faturamento Total (R$)"].min()
    dffatm = dados[dados["Faturamento Total (R$)"] == fattmin]
    print("\nPRODUTO COM MENOR FATURAMENTO:")
    print(dffatm[["Produto", "Faturamento Total (R$)"]])

    # Filtering and displaying only values with low satisfaction:
    dfsat = dados[dados["Satisfação"] == "Baixo"]
    print("\nPRODUTOS COM BAIXA SATISFAÇÃO:")

    # Print only specific columns (Passing value as a list)
    print(dfsat[["Produto", "Satisfação"]])

except Exception as e:
    print(f"Erro {e}")
    exit()
