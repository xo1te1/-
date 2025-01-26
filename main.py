import pandas as pd

chunksize = 1000
for chunk in pd.read_csv('sales_data.csv', chunksize=chunksize):
    unique_values = chunk['product'].nunique()
print("Кількість унікальних продуктів: ", unique_values)
