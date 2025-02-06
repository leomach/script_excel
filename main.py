
import os
from process import processar_escolas, processar_saidas

# Defina o caminho onde estão as pastas das escolas
base_dir = "./diario"  # Ajuste esse caminho
base_saida = "./saida" # Ajuste esse caminho

# Lista as escolas
escolas = os.listdir(base_dir)



# Processa as escolas
# processar_escolas(escolas, base_dir)

processar_saidas(base_saida)