
import os
import pandas as pd # type: ignore

def clean_screen():
    """Clear the screen based on the operating system."""
    os.system("cls" if os.name == "nt" else "clear")

def open_file(caminho_arquivo):

    if os.path.exists(caminho_arquivo):

        # Verifica se o arquivo é CSV ou Excel
        if caminho_arquivo.endswith(".csv"):
            df = pd.read_csv(caminho_arquivo, encoding="utf-8", sep=";")
        elif caminho_arquivo.endswith(".xlsx") or caminho_arquivo.endswith(".xls"):
            df = pd.read_excel(caminho_arquivo, engine="openpyxl")
        else:
            print(f"Formato não suportado: {caminho_arquivo}")
            df = None
    else:
        print(f"ERRO: Arquivo não encontrado -> {caminho_arquivo}")
        df = None

    return df
