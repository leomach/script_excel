import os
from tqdm import tqdm # type: ignore
from students import students_archives
from teams import team_archives
from schools import school_archives
from exit_process.profission import dataframe_profissions

def listar_arquivos(diretorio, extensao=".xlsx"):
    """Lista arquivos com a extensão especificada dentro do diretório."""
    return [f for f in os.listdir(diretorio) if f.endswith(extensao)]

def processar_arquivos(diretorio, arquivos, tipo, escola, base_dir):
    """Processa os arquivos e exibe barra de progresso."""
    if arquivos:
        print(f"  📂 {tipo}:")
        for arquivo in tqdm(arquivos, desc=f" Processando {tipo.lower()}", unit="arquivo"):
            print(f"    📄 {arquivo}")
            # Chama a função para processamento dos arquivos
            if tipo == "Estudantes":
                students_archives(escola, arquivo, base_dir)
            elif tipo == "Professores":
                team_archives(escola, arquivo, base_dir)

def processar_escola(escola, base_dir):
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
            processar_arquivos(pasta_estudantes, arquivos_estudantes, "Estudantes", escola, base_dir)

        # Listar e processar arquivos de professores
        if os.path.exists(pasta_professores):
            arquivos_professores = listar_arquivos(pasta_professores)
            processar_arquivos(pasta_professores, arquivos_professores, "Professores", escola, base_dir)

def processar_escolas(escolas, base_dir):
    """Processa todas as escolas com barra de progresso."""
    for escola in tqdm(escolas, desc="Processando escolas", unit="escola"):
        processar_escola(escola, base_dir)
        os.system("cls" if os.name == "nt" else "clear") # Limpar tela de acordo com o OS

    school_archives(base_dir)




"""
FUNÇÕES DE TRATAMENTO DA SAÍDA
"""
def processar_arquivos_saida(arquivos, categoria, base_dir):
    """Processa os arquivos da saida e exibe barra de progresso."""
    
    if arquivos:
        for arquivo in tqdm(arquivos, desc=f" Processando {categoria.lower()}", unit="arquivo"):
            # Chama a função para processamento dos arquivos
            if categoria == "alunos":
                pass
            elif categoria == "responsaveis":
                pass
            elif categoria == "profissoes":
                dataframe_profissions(arquivo)
            elif categoria == "equipes":
                pass
            elif categoria == "professores":
                pass
            elif categoria == "turmas":
                pass
            elif categoria == "escolas":
                pass

def processar_saidas (base_saida):
    arquivos_saida = listar_arquivos(base_saida, extensao=".csv")
    # Criando dicionário para armazenar os arquivos separados
    categorias = {
        "alunos": [],
        "profissoes": [],
        "responsaveis": [],
        "equipes": [],
        "professores": [],
        "turmas": [],
        "escolas": []
    }

    # Percorrer a lista e separar os arquivos
    for arquivo in tqdm(arquivos_saida, desc="Carregando as saidas", unit="arquivo"):
        if arquivo.startswith("alunos-"):
            categorias["alunos"].append(arquivo)
        elif arquivo.startswith("profissoes-"):
            categorias["profissoes"].append(arquivo)
        elif arquivo.startswith("responsaveis-"):
            categorias["responsaveis"].append(arquivo)
        elif arquivo.startswith("equipe-"):
            categorias["equipes"].append(arquivo)
        elif arquivo.startswith("professores-"):
            categorias["professores"].append(arquivo)
        elif arquivo.startswith("turmas"):
            categorias["turmas"].append(arquivo)
        elif arquivo.startswith("escolas"):
            categorias["escolas"].append(arquivo)

    # Exibir os resultados
    for categoria, lista in categorias.items():
        print(f"\n📂 {categoria.capitalize()} ({len(lista)} arquivos):")
        print(lista)

    # Processar arquivos na ordem correta de categorias
    processar_arquivos_saida(categorias["profissoes"], "profissoes", base_saida)
    print("")