import pandas as pd
import re
import json
import numpy as np

dados = pd.read_csv("data/informacoes-smartphones.csv", encoding="utf-8", sep=";")


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


def encontra_palavra(titulo, lista):

    flag = [elemento for elemento in lista if elemento.lower() + " " in titulo.lower()]

    if flag:
        return str(flag)[1:-1]
    else:
        return ""


def cor(df):

    with open("data/filtros.json", "r") as file:
        data = json.load(file)

    cores = data["cores"]

    df["cor"] = df["titulo"].apply(lambda titulo: encontra_palavra(titulo, cores))
    df["cor"] = df["cor"].str.replace("'", "")

    return df


def marca(df):

    with open("data/filtros.json", "r") as file:
        data = json.load(file)

    marca = data["marcas"]

    df["marca"] = df["titulo"].apply(lambda titulo: encontra_palavra(titulo, marca))
    df["marca"] = df["marca"].str.replace("'", "")

    return df


def verifica_estado(titulo, lista):
    flag = [elemento for elemento in lista if elemento.lower() in titulo.lower()]

    if flag:
        return str(flag)[1:-1]
    else:
        return "Novo"


def estado(df):

    estado = ["Usado"]

    df["estado"] = df["titulo"].apply(lambda titulo: verifica_estado(titulo, estado))
    df["estado"] = df["estado"].str.replace("'", "")

    return df


def transform(df) -> pd.DataFrame:

    df = memoria_ram(df)
    df = armazenamento(df)
    df = cor(df)
    df = marca(df)
    df = estado(df)

    return df


df = transform(dados)
df.to_csv("data/teste.csv", index=False, sep=";", encoding="utf-8")
