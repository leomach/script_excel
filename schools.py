import os
import json
import pandas as pd # type: ignore
from cities import remove_duplicate_keys, cities

# Definir o caminho onde os arquivos serão salvos
global caminho_saida
caminho_saida = "./saida/"
# Garantir que o diretório existe
os.makedirs(caminho_saida, exist_ok=True)

def schools(df_schools_classrooms):
    global caminho_saida

    schools = df_schools_classrooms[['Escola', 'id']].copy()
    schools.rename(columns={'Escola' : 'name', 'id': 'id_turma'}, inplace=True)

    # Remover espaços no início e no final das strings, e eliminar espaços duplicados nas colunas relevantes
    schools['name'] = schools['name'].str.strip().str.replace(r'\s+', ' ', regex=True)

    # Substituir NaN por uma string vazia (caso queira ignorar as células NaN)
    schools.replace({'': pd.NA, 'Não Informado': pd.NA}, inplace=True)

    schools.dropna(subset=['name'], inplace=True)

    # Agrupar os ids de turmas de escolas duplicados separando-os por vírgula
    schools = schools.groupby(['name'], as_index=False).agg({
        'id_turma': lambda x: ', '.join(x.astype(str).dropna())  # Concatena as IDs de estudantes
    })

    schools['school'] = range(1, len(schools) + 1)

    schools_exploded = schools.copy().assign(
        id_turma=schools['id_turma'].astype(str).str.split(', ')
    ).explode('id_turma')

    # Converter IDs para int, substituindo NaN por 0
    schools_exploded['id_turma'] = schools_exploded['id_turma'].fillna(0).astype(int)
    schools_exploded['school'] = schools_exploded['school'].fillna(0).astype(int)

    # Fazer merge novamente garantindo que todos as turmas tenham escola
    df_school_with_classroom = pd.merge(df_schools_classrooms, schools_exploded[['id_turma', 'school']], left_on='id', right_on='id_turma', how='left')
    df_escola_com_turma = df_school_with_classroom[['id', 'description', 'shift', 'capacity', 'school']].copy()

    # Preparar para impressão
    schools_print = schools[['school', 'name']].copy()
    schools_print.rename(columns={'school': 'id',}, inplace=True)

    # Salvar o DataFrame como um arquivo CSV
    schools_print.to_csv(f"{caminho_saida}escolas.csv", index=False, encoding="utf-8-sig", sep=";")

    return df_escola_com_turma


def school_archives(base_dir):
    global caminho_saida
    
    # Caminho para um dos arquivos de estudantes (ajuste conforme necessário)
    caminho_arquivo = f"{base_dir}/escolas_e_turmas.xlsx"

    # Ler o arquivo Excel
    df_schools_classrooms = pd.read_excel(caminho_arquivo, engine="openpyxl")

    # Colocando a tipagem de inteiro nas colunas
    df_schools_classrooms['Ord.'] = df_schools_classrooms['Ord.'].fillna(0).astype(int)
    df_schools_classrooms['Tot. Estudantes'] = df_schools_classrooms['Tot. Estudantes'].fillna(0).astype(int)

    df_schools_classrooms.rename(columns={'Turma': 'description', 'Tot. Estudantes': 'capacity', 'Turno': 'shift'}, inplace=True)

    # Criar uma coluna de ID único
    df_schools_classrooms['id'] = range(1, len(df_schools_classrooms) + 1)

    def_classrooms = schools(df_schools_classrooms)
    
    def_classrooms['shift'] = def_classrooms['shift'].map({'Manhã': "1", 'Tarde': "2", "Integral": "4"}).fillna(def_classrooms['shift'])

    # Salvar o DataFrame como um arquivo CSV
    def_classrooms.to_csv(f"{caminho_saida}turmas.csv", index=False, encoding="utf-8-sig", sep=";")