import os
from tqdm import tqdm # type: ignore
from students import students_archives, students_archives_unify
from teams import team_archives, team_archives_unify
from schools import school_archives
from utils.functions import entry_dir
from students import DATAFRAMES_STUDENTS

def listar_arquivos(diretorio, extensao=".xlsx"):
    """Lista arquivos com a extensão especificada dentro do diretório."""
    return [f for f in os.listdir(diretorio) if f.endswith(extensao)]

def processar_arquivos(diretorio, arquivos, tipo, escola, base_dir, unify=False):
    """Processa os arquivos e exibe barra de progresso."""
    if arquivos:
        print(f"  📂 {tipo}:")
        for arquivo in tqdm(arquivos, desc=f" Processando {tipo.lower()}", unit="arquivo"):
            print(f"    📄 {arquivo}")
            # Chama a função para processamento dos arquivos
            if tipo == "Estudantes" and unify == False:
                students_archives(escola, arquivo, base_dir)
            elif tipo == "Professores" and unify == False:
                pass
                team_archives(escola, arquivo, base_dir)
            elif tipo == "Estudantes" and unify == True:
                students_archives_unify(escola, arquivo, base_dir)
            elif tipo == "Professores" and unify == True:
                pass
                team_archives_unify(escola, arquivo, base_dir)

def processar_escola(escola, base_dir, unify=False):
    """Processa uma escola, verificando suas subpastas e arquivos."""
    escola_path = os.path.join(base_dir, escola)

    # Verifica se é uma pasta
    if os.path.isdir(escola_path):
        print(f"\n📁 Escola: {escola}")

        # Caminhos das subpastas
        pasta_estudantes = os.path.join(escola_path, "Estudantes")
        pasta_professores = os.path.join(escola_path, "Professores")

        # Listar e processar arquivos de estudantes
        if os.path.exists(pasta_estudantes):
            arquivos_estudantes = listar_arquivos(pasta_estudantes)
            processar_arquivos(pasta_estudantes, arquivos_estudantes, "Estudantes", escola, base_dir, unify=unify)

        # Listar e processar arquivos de professores
        if os.path.exists(pasta_professores):
            arquivos_professores = listar_arquivos(pasta_professores)
            processar_arquivos(pasta_professores, arquivos_professores, "Professores", escola, base_dir, unify=unify)


def processar_escolas(escolas, base_dir, entrada_dir):

    """Cria a pasta de entrada."""
    base_entrada = entry_dir(entrada_dir)
    listar_arquivos = os.listdir(base_entrada)

    """Une todas as escolas com barra de progresso."""
    for escola in tqdm(escolas, desc="Unindo escolas", unit="escola"):
        processar_escola(escola, base_dir, unify=True)
        print("")

    print("\n================================================================")
    """Processa arquivo unificado"""
    for arquivo in listar_arquivos:
        print("######### Processando arquivo unificado... #########")
        processar_escola(arquivo, base_entrada)

    # school_archives(base_dir)