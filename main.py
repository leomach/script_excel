
import os
from process import processar_escolas

# Defina o caminho onde estão as pastas das escolas
base_dir = "./diario"  # Ajuste esse caminho
base_entrada = "./entrada" # Ajuste esse caminho

# Lista as escolas
escolas = os.listdir(base_dir)



# Processa as escolas
processar_escolas(escolas, base_dir, base_entrada)