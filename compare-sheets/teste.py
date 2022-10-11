
# Importing Libraries
import pandas as pd
import numpy as np
 
# data's stored in dictionary
details = {
    'Codigo': [1, 3, 30, 4],
    'Quantidade': [31, 8, 10, 30]
}
planilha02 = {
    'Codigo': [10, 2, 50, 70],
    'Quantidade': [31, 8, 10, 30]
}
 
# creating a Dataframe object

df = pd.DataFrame(details)
df2  = pd.DataFrame(planilha02)

output = pd.Series()

# Where method to compare the values
# The values were stored in the new column


# output['Códigos Alterados'] = np.where((df2['Codigo'] != df['Codigo']), df2['Codigo'], np.nan)
# output['Quantidade Alteradas'] = np.where((df2['Quantidade'] != df['Quantidade']), df2['Quantidade'], np.nan)

# ---
codigos01 = []
qtd01 = []

codigos02 = []
qtd02 = []
saidacod = []
saidaqtd = []

for index, row in df.iterrows():
    codigos01.append(row[df.columns.to_list()[0]])
    qtd01.append(row[df.columns.to_list()[1]])

for index, row in df2.iterrows():
    codigos02.append(row[df2.columns.to_list()[0]])
    qtd02.append(row[df2.columns.to_list()[1]])	


print(codigos01, "!!!!!!!!!!!!!!!")
for j in codigos01:
    for k in codigos02:
        # output['Códigos Alterados'] = np.where((j != k), k, np.nan)
        saidacod.append(np.where((j != k), k, np.nan))
for l in qtd01:
    for a in qtd02:
        # fazer uma lista para a saida 
        # output['Quantidade Alterados'] = np.where((l != a), f'{l} e {a}', a)
        saidaqtd.append(np.where((l != a), f'{l} e {a}', a))

# printing the dataframe
print(df, " = = = = == PLANILHA 01")
print(df2, " = = = = == PLANILHA 02")

print(output, " = = = = a")
# print(saidaqtd)
print(saidacod)