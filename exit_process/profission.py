import pandas as pd # type: ignore
import os
from utils.functions import open_file

from .core import (
    DATAFRAMES_PROFISSION,
)

def dataframe_profissions(arquivo):
    global DATAFRAMES_PROFISSION

    caminho_arquivo = f"./saida/{arquivo}"

    df_profission = open_file(caminho_arquivo)

    # Renomeando a coluna "id" do dataframe
    if "id" in df_profission.columns:
        df_profission = df_profission.rename(columns={'id': 'id_profission_legacy'})
    else:
        print("Coluna 'id' não encontrada, pulando rename.")

    # Unificando o dataframe com os já encontrados
    if DATAFRAMES_PROFISSION is None or DATAFRAMES_PROFISSION.empty:
        DATAFRAMES_PROFISSION = df_profission
        print("Dataframe de profissões inicializado.")
    else:
        DATAFRAMES_PROFISSION = pd.concat([DATAFRAMES_PROFISSION, df_profission], ignore_index=True)
    
    print(DATAFRAMES_PROFISSION)