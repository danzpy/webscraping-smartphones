import pandas as pd
import re

dados = pd.read_csv("data/informacoes-smartphones.csv", encoding="utf-8", sep=";")

# print(
#     dados[
#         ~dados["titulo"].str.contains(r"\b(1[0-2]|[1-9])gb\b", case=False, regex=True)
#     ]
# )

# Utilizar metodo .extract para coletar informação e adiciona-la em uma nova coluna.


def memoria_ram(df):

    # O padrão abaixo foi encontrado com auxílio de inteligência artificial.
    pattern = r"\b(1[0-2]|[1-9])gb\b"

    df["ram"] = df["titulo"].str.extract(pattern, flags=re.IGNORECASE)

    return df


ram = memoria_ram(dados)
ram.to_csv("data/teste.csv", index=False, sep=";", encoding="utf-8")
