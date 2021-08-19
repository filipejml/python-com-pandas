# -*- coding: utf-8 -*-
"""PlanilhasExcel.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1AlDsPpPkxkdT0gs5tJQ2G2OKxa_BQOe0
"""

import pandas as pd

df1 = pd.read_excel("Aracaju.xlsx")
df2 = pd.read_excel("Fortaleza.xlsx")
df3 = pd.read_excel("Natal.xlsx")
df4 = pd.read_excel("Recife.xlsx")
df5 = pd.read_excel("Salvador.xlsx")

df1.head()

df = pd.concat([df1, df2, df3, df4, df5])

df.head()

df.tail()

df.sample(5)

df.dtypes

df["LojaID"] = df["LojaID"].astype("object")

df.dtypes

df.isnull().sum()



df["Receita"].max()

df["Data"] = df{"Data"}.astype("int64")

df.dtypes

df("Receita") = df("Vendas") * df("Qtde")

Receita = "Vendas" * "Qtde"

df["Receita"] = df["Vendas"].mul(df["Qtde"])

df.head()

df["Receita"].max()

df["Receita"].min()

df.nlargest(10, "Receita")

df.nsmallest(10, "Receita")

df.groupby("Cidade")["Receita"].sum()

df.sort_values("Receita", ascending=False).head(50)

df.groupby(df["Data"].dt.year)["Receita"].sum()

df.groupby(df["Data"].dt.month)["Receita"].sum()

df["Ano de Venda"] = df["Data"].dt.year

df.head(10)

df.sample(5)

df["Mes de Venda"], df["Dia de Venda"] = (df["Data"].dt.month, df["Data"].dt.day)

df.head(10)

df.sample(5)

df["Data"].min

df["dif de dias"] = df["Data"] - df["Data"].min()

df.head(10)

df.sample(5)

df["Trimestre"] = df["Data"].dt.quarter

df.sample(10)

vendas_abril_2019 = df.loc[(df["Data"].dt.year == 2019) & (df["Data"].dt.month == 4)]

vendas_abril_2019

df["LojaID"].value_counts(ascending=False)

df["LojaID"].value_counts(ascending=False).plot.bar()

df["LojaID"].value_counts(ascending=True).plot.barh();

df.groupby(df["Data"].dt.year)["Receita"].sum().plot.pie()

#Colocando titulo e nome nos eixos
import matplotlib.pyplot as plt
df["Cidade"].value_counts().plot.bar(title = "Total de Vendas por cidade", color = "red")
plt.xlabel("Cidade")
plt.ylabel("Total Vendas")

plt.style.use("ggplot")

df.groupby(df["Mes de Venda"])["Qtde"].sum().plot(title = "total produtos x mês")
plt.xlabel("Mes")
plt.ylabel("Total Produtos Vendidos")
plt.legend()

df.groupby(df["Mes de Venda"])["Qtde"].sum()

df_2019 = df[df["Ano de Venda"] == 2019]

plt.hist(df["Qtde"], color = "pink")

plt.scatter(x = df_2019["Dia de Venda"], y = df_2019["Receita"]);
plt.savefig("dispersão.png")

