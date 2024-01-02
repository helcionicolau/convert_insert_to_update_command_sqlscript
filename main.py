import re

# Função para extrair os valores do INSERT
def extrair_valores_insert(insert_query):
    match = re.search(r"\((.*?)\)", insert_query)
    if match:
        valores = match.group(1).split(', ')
        return valores
    return None

# Função para criar comando UPDATE a partir dos valores extraídos
def gerar_comando_update(valores):
    atm_sigit_code = valores[1]
    lat = valores[-2]
    long = valores[-1]
    
    comando_update = f"UPDATE `atm` SET `lat` = {lat}, `long` = {long} WHERE atm_sigit_code = '{atm_sigit_code}';"
    return comando_update

# Ler o arquivo de texto com a codificação 'utf-8'
with open('atm_update.txt', 'r', encoding='utf-8') as file:
    conteudo = file.read()

# Dividir o conteúdo em comandos
comandos = conteudo.split('),\n\n')

# Lista para armazenar os comandos UPDATE gerados
comandos_update = []

# Processar cada comando
for comando in comandos:
    valores_insert = extrair_valores_insert(comando)
    if valores_insert:
        comando_update = gerar_comando_update(valores_insert)
        comandos_update.append(comando_update)

# Gravar os comandos UPDATE em um arquivo de texto
with open('comandos_update.txt', 'a', encoding='utf-8') as file:
    for comando_update in comandos_update:
        file.write(comando_update + '\n')
