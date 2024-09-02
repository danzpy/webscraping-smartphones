import pandas as pd
import re

dados = pd.read_csv("data/informacoes-smartphones.csv", encoding="utf-8", sep="|")

print(
    dados[
        ~dados["titulo"].str.contains(r"\b(1[0-2]|[1-9])gb\b", case=False, regex=True)
    ]
)

# Utilizar metodo .extract para coletar informação e adiciona-la em uma nova coluna.
