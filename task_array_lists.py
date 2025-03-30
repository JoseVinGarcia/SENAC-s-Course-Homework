# Clothing Store Inventory
import pandas as pd

# create a list with values
produtos = ["Camiseta", "Calça", "Jaqueta", "Vestido", "Boné"]
quantidade = [50,30,15,10,25]

# Turn into a series
sestoque = pd.Series(quantidade, index = produtos)

# Add a null value
sestoque.loc["Saia"] = None

# Show the entire stock
print("="*30)
print("ESTOQUE TOTAL:")
print(sestoque)

# Show products with more than 20 units
print("\nPRODUTOS COM MAIS DE UNIDADE:")
print(sestoque[sestoque>20])

# Add values
svalores=pd.Series([3500, 2500, 1200, 900, 1500], index=produtos)

# Show the stock now with values
print("\nPRODUTOS COM PREÇO:")
print(svalores)

# Show the total value of the stock
print("\nVALOR TOTAL DO ESTOQUE:")
print(sestoque * svalores)
