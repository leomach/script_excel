
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

def entry_dir(base_entrada):
    # Faz a pasta de entrada para colocar os arquivos da unificação
    if not os.path.exists(base_entrada):
        os.makedirs(base_entrada)
        print(f"\n�� Criando pasta de entrada: {base_entrada}")
    else:
        print(f"\n�� Pasta de entrada já existe: {base_entrada}")
    
    # Criar pasta "TODOS OS DADOS"
    todos_dados_dir = os.path.join(base_entrada, "TODOS OS DADOS")
    if not os.path.exists(todos_dados_dir):
        os.makedirs(todos_dados_dir)
        print(f"\n�� Criando pasta 'TODOS OS DADOS': {todos_dados_dir}")
    else:
        print(f"\n�� Pasta 'TODOS OS DADOS' já existe: {todos_dados_dir}")
    
    # Criar pasta "Estudantes" na pasta "TODOS OS DADOS"
    estudantes_dir = os.path.join(todos_dados_dir, "Estudantes")
    if not os.path.exists(estudantes_dir):
        os.makedirs(estudantes_dir)
        print(f"\n�� Criando pasta 'Estudantes': {estudantes_dir}")
    else:
        print(f"\n�� Pasta 'Estudantes' já existe: {estudantes_dir}")
    
    # Criar pasta "Professores" na pasta "TODOS OS DADOS"
    professores_dir = os.path.join(todos_dados_dir, "Professores")
    if not os.path.exists(professores_dir):
        os.makedirs(professores_dir)
        print(f"\n�� Criando pasta 'Professores': {professores_dir}")
    else:
        print(f"\n�� Pasta 'Professores' já existe: {professores_dir}")

    return base_entrada
