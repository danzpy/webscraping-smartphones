import pandas as pd
import re

dados = pd.read_csv("data/informacoes-smartphones.csv", encoding="utf-8", sep=";")

# print(
#     dados[
#         ~dados["titulo"].str.contains(r"\b(1[0-2]|[1-9])gb\b", case=False, regex=True)
#     ]
# )

# Utilizar metodo .extract para coletar informação e adiciona-la em uma nova coluna.


def memoria_ram(df) -> pd.DataFrame:

    # O padrão abaixo foi encontrado com auxílio de inteligência artificial.
    pattern = r"\b(1[0-2]|[1-9])gb\b"

    df["ram (gb)"] = df["titulo"].str.extract(pattern, flags=re.IGNORECASE)

    return df


def armazenamento(df) -> pd.DataFrame:

    # O padrões abaixo foram encontrados com auxílio de inteligência artificial.
    # pattern_gb = r"\b([1-9]\d{1,2}|1[6-9])\s*[gG][bB]\b"
    pattern_gb = r"\b(1[6-9]|[2-9]\d|\d{3})\s*[gG][bB]\b"
    pattern_tb = r"\b1\s*[tT][bB]\b"

    df["armazenamento (gb)"] = df["titulo"].str.extract(pattern_gb, flags=re.IGNORECASE)

    df.loc[
        df["titulo"].str.contains(pattern_tb, flags=re.IGNORECASE), "armazenamento (gb)"
    ] = "1024"

    return df


def transform(df) -> pd.DataFrame:

    df = memoria_ram(df)
    df = armazenamento(df)

    return df


df = transform(dados)
df.to_csv("data/teste.csv", index=False, sep=";", encoding="utf-8")
