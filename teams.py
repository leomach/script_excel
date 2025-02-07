import os
import pandas as pd # type: ignore

# Definir o caminho onde os arquivos serão salvos
global caminho_saida
caminho_saida = "./saida/"
# Garantir que o diretório existe
os.makedirs(caminho_saida, exist_ok=True)

def team_archives(escola, arquivo, base_dir):
    global caminho_saida
    # Caminho para um dos arquivos de estudantes (ajuste conforme necessário)
    caminho_arquivo = f"{base_dir}/{escola}/Professores/{arquivo}"

    df_team = pd.read_excel(caminho_arquivo, engine="openpyxl", skiprows=6)
    df_teams = df_team[["CPF", "Nome", "Função", "Telefone", "Email", "Observação"]].copy()

    # Dividindo por função
    df_professores = df_teams[df_teams["Função"].isin(["EDUCADOR", "Educador (a)", "Educador(a)", "Mediador", "Mediador(a)", "Mediadora", "Monitora", "PROFESSOR", "Professora"])].copy()
    df_adm = df_teams[df_teams["Função"].isin(["Administrador", "AUX. DE SECRETARIA", "Diretor", "DIRETOR ADJUNTO", "Diretora", "DIRETORA ADJUNTA", "Diretora Adjunta", "GESTOR", "GESTORA", "SECRETARIA", "Secretária", "TEC. SECRETARIA", "Técnica de secretaria", "Técnico Administrativo", "TECNICO DE SECRETARIA", "Técnico de Secretaria", "Técnico(a) de Secretaria"])].copy()
    df_coordenadores = df_teams[df_teams["Função"].isin(["Coodenador(a)", "Coordenador", "Coordenador(a)", "Coordenadora", "Coordenadora Pedagógica",])].copy()

    # Ajustando IDs de função
    df_professores.loc[:, "Função"] = "01"
    df_adm.loc[:, "Função"] = "04"
    df_coordenadores.loc[:, "Função"] = "01"

    df_teams = pd.concat([df_adm, df_coordenadores], ignore_index=True)

    # Ajustando nomes das colunas
    df_teachers = df_professores.copy().rename(columns={"CPF": "cpf", "Nome": "name", "Função": "type", "Telefone": "celphone_1", "Email": "email", "Observação": "note"})
    df_teams = df_teams.rename(columns={"CPF": "cpf", "Nome": "name", "Função": "team_type", "Telefone": "celphone_1", "Email": "email", "Observação": "note"})

    df_teachers['id'] = range(1, len(df_teachers) + 1)
    df_teams['id'] = range(1, len(df_teams) + 1)

    # Adicionando login e password de acordo com o CPF
    df_teachers['login'] = df_teachers['cpf']
    df_teachers['password'] = df_teachers['cpf']
    df_teams['login'] = df_teams['cpf']
    df_teams['password'] = df_teams['cpf']

    # Salvando os DataFrames como arquivos CSV
    df_teachers.to_csv(f"{caminho_saida}professores-{escola}.csv", index=False, encoding="utf-8-sig", sep=";")
    df_teams.to_csv(f"{caminho_saida}equipe-{escola}.csv", index=False, encoding="utf-8-sig", sep=";")

def team_archives_unify(escola, arquivo, base_dir):
    print(escola, arquivo, base_dir)