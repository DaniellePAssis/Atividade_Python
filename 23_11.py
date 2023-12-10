#1.Calcular quantas publicações
#2.Extrair lista das tags
#3.Extrair número das tags e de ocorrências das respectivas tags
#4.Extrair gamas de datas que constam no ficheiro, quando começam e terminam
#5.Inventar alguma coisa para extrair do texto. Exercício livre


#1.Calcular quantas publicações
def contar_publicacoes(nome_arquivo):
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            conteudo = arquivo.read()
            numero_de_publicacoes = conteudo.count('<pub>')
            return numero_de_publicacoes
    except FileNotFoundError:
        return "Arquivo não encontrado"
    except Exception as e:
        return f"Ocorreu um erro: {str(e)}"

if __name__ == "__main__":
    nome_arquivo = "folha8.OUT.txt"  
    numero_de_publicacoes = contar_publicacoes(nome_arquivo)
    
    if isinstance(numero_de_publicacoes, int):
        print(f"O arquivo contém {numero_de_publicacoes} publicações identificadas como <pub>.")
    else:
        print(numero_de_publicacoes)


#2.Extrair lista das tags
import re

def extrair_tags(nome_arquivo):
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            conteudo = arquivo.read()
            padrao_tags = r'#TAG:\s*([^\n]+)'
            tags_encontradas = re.findall(padrao_tags, conteudo)
            return tags_encontradas
    except FileNotFoundError:
        return "Arquivo não encontrado"
    except Exception as e:
        return f"Ocorreu um erro: {str(e)}"

if __name__ == "__main__":
    nome_arquivo = "folha8.OUT.txt"  
    tags_encontradas = extrair_tags(nome_arquivo)
    
    if tags_encontradas:
        print("Tags encontradas:")
        for tag in tags_encontradas:
            print(tag)
    else:
        print("Nenhuma tag encontrada no arquivo.")

#2.Extrair lista das tags em outro arquivo

import re

def extrair_tags(nome_arquivo_entrada):
    try:
        with open(nome_arquivo_entrada, 'r', encoding='utf-8') as arquivo:
            conteudo = arquivo.read()
            padrao_tags = r'#TAG:\s*([^\n]+)'
            tags_encontradas = re.findall(padrao_tags, conteudo)
            return tags_encontradas
    except FileNotFoundError:
        return "Arquivo de entrada não encontrado"
    except Exception as e:
        return f"Ocorreu um erro: {str(e)}"

def salvar_tags_em_arquivo(tags, nome_arquivo_saida):
    try:
        with open(nome_arquivo_saida, 'w', encoding='utf-8') as arquivo:
            for tag in tags:
                arquivo.write(tag + '\n')
        return True
    except Exception as e:
        return f"Erro ao salvar as tags: {str(e)}"

if __name__ == "__main__":
    nome_arquivo_entrada = "folha8.OUT.txt"  
    nome_arquivo_saida = "Lista de tags.txt"  

    tags_encontradas = extrair_tags(nome_arquivo_entrada)

    if tags_encontradas:
        print("Tags encontradas:")
        for tag in tags_encontradas:
            print(tag)

        sucesso = salvar_tags_em_arquivo(tags_encontradas, nome_arquivo_saida)

        if sucesso:
            print(f"As tags foram salvas em {nome_arquivo_saida}.")
        else:
            print("Erro ao salvar as tags.")
    else:
        print("Nenhuma tag encontrada no arquivo de entrada.")


#3.Extrair número das tags e de ocorrências das respectivas tags

import re

def contar_ocorrencias_das_tags(nome_arquivo):
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            conteudo = arquivo.read()
            padrao_tags = r'tag:\{\s*(\d+)\s*\}'
            matches = re.findall(padrao_tags, conteudo)
            
            numeros_ocorrencias = [int(numero) for numero in matches]
            total_ocorrencias = sum(numeros_ocorrencias)
            return total_ocorrencias
    except FileNotFoundError:
        return "Arquivo não encontrado"
    except Exception as e:
        return f"Ocorreu um erro: {str(e)}"

if __name__ == "__main__":
    nome_arquivo = "folha8.OUT.txt"  

    total_ocorrencias = contar_ocorrencias_das_tags(nome_arquivo)

    if isinstance(total_ocorrencias, int):
        print(f"O número total de ocorrências das tags é: {total_ocorrencias}")
    else:
        print(total_ocorrencias)


#3.Extrair ocorrências das respectivas tags em arquivo.txt

import re
from collections import Counter

def contar_tags_com_conteudo(nome_arquivo):
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            conteudo = arquivo.read()

            # Expressão regular mais geral para capturar tags com diversos conteúdos
            padrao_tags = re.compile(r'tag:{(.*?)}')
            tags_encontradas = padrao_tags.findall(conteudo)

            # Usando Counter para contar a ocorrência de cada tag com mesmo conteúdo
            contagem_tags = Counter(tags_encontradas)

            return contagem_tags
    except FileNotFoundError:
        return "Arquivo não encontrado"
    except Exception as e:
        return f"Ocorreu um erro: {str(e)}"

def salvar_lista_tags(nome_arquivo_saida, contagem_tags):
    try:
        with open(nome_arquivo_saida, 'w', encoding='utf-8') as arquivo_saida:
            for tag, quantidade in contagem_tags.items():
                arquivo_saida.write(f"tag:{tag}: {quantidade}\n")
        return f"Lista de tags salva em {nome_arquivo_saida}"
    except Exception as e:
        return f"Ocorreu um erro ao salvar a lista de tags: {str(e)}"

if __name__ == "__main__":
    nome_arquivo_entrada = "folha8.OUT.txt" 
    nome_arquivo_saida = "Contagem_das_tags.txt"     

    contagem_tags = contar_tags_com_conteudo(nome_arquivo_entrada)

    if isinstance(contagem_tags, Counter):
        print("Contagem de tags com mesmo conteúdo:")
        for tag, quantidade in contagem_tags.items():
            print(f"tag:{tag}: {quantidade}")

        resultado_salvar = salvar_lista_tags(nome_arquivo_saida, contagem_tags)
        print(resultado_salvar)
    else:
        print(contagem_tags)



#4.Extrair gamas de datas que constam no ficheiro, quando começam e terminam

import re

def extrair_gamas_de_datas(nome_arquivo):
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            conteudo = arquivo.read()
            padrao_gama = r'(\d{1,2}) de ([A-Za-zçãõéíóú]+) de (\d{4})'
            matches = re.findall(padrao_gama, conteudo)
            
            gamas_de_datas = [(int(dia), mes, int(ano)) for dia, mes, ano in matches]
            return gamas_de_datas
    except FileNotFoundError:
        return "Arquivo não encontrado"
    except Exception as e:
        return f"Ocorreu um erro: {str(e)}"

if __name__ == "__main__":
    nome_arquivo = "folha8.OUT.txt"  

    gamas_de_datas = extrair_gamas_de_datas(nome_arquivo)

    if gamas_de_datas:
        print("Gamas de datas encontradas:")
        for dia, mes, ano in gamas_de_datas:
            print(f"{dia} de {mes} de {ano}")
    else:
        print("Nenhuma gama de datas encontrada no arquivo.")

#Número de ocorrÊncias formato dd/mm/aaaa

import re

def extrair_gamas_de_datas(nome_arquivo):
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            conteudo = arquivo.read()
            padrao_gama = r'(\d{2}/\d{2}/\d{4})\s*-\s*(\d{2}/\d{2}/\d{4})'
            matches = re.findall(padrao_gama, conteudo)
            
            gamas_de_datas = [(inicio, fim) for inicio, fim in matches]
            return gamas_de_datas
    except FileNotFoundError:
        return "Arquivo não encontrado"
    except Exception as e:
        return f"Ocorreu um erro: {str(e)}"

if __name__ == "__main__":
    nome_arquivo = "folha8.OUT.txt"  

    gamas_de_datas = extrair_gamas_de_datas(nome_arquivo)

    if gamas_de_datas:
        print("Gamas de datas encontradas:")
        for inicio, fim in gamas_de_datas:
            print(f"De {inicio} a {fim}")
    else:
        print("Nenhuma gama de datas encontrada no arquivo.")

#Número de ocorrÊncias formato dd-mm-aaaa
import re

def extrair_gamas_de_datas(nome_arquivo):
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            conteudo = arquivo.read()
            padrao_gama = r'(\d{2}-\d{2}-\d{4})\s*-\s*(\d{2}-\d{2}-\d{4})'
            matches = re.findall(padrao_gama, conteudo)
            
            gamas_de_datas = [(inicio, fim) for inicio, fim in matches]
            return gamas_de_datas
    except FileNotFoundError:
        return "Arquivo não encontrado"
    except Exception as e:
        return f"Ocorreu um erro: {str(e)}"

if __name__ == "__main__":
    nome_arquivo = "folha8.OUT.txt"  

    gamas_de_datas = extrair_gamas_de_datas(nome_arquivo)

    if gamas_de_datas:
        print("Gamas de datas encontradas:")
        for inicio, fim in gamas_de_datas:
            print(f"De {inicio} a {fim}")
    else:
        print("Nenhuma gama de datas encontrada no arquivo.")


#Número de ocorrÊncias formato dd/mm

import re

def extrair_gamas_de_datas(nome_arquivo):
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            conteudo = arquivo.read()
            padrao_gama = r'(\d{2}/\d{2})\s*-\s*(\d{2}/\d{2})'
            matches = re.findall(padrao_gama, conteudo)
            
            gamas_de_datas = [(inicio, fim) for inicio, fim in matches]
            return gamas_de_datas
    except FileNotFoundError:
        return "Arquivo não encontrado"
    except Exception as e:
        return f"Ocorreu um erro: {str(e)}"

if __name__ == "__main__":
    nome_arquivo = "folha8.OUT.txt"  

    gamas_de_datas = extrair_gamas_de_datas(nome_arquivo)

    if gamas_de_datas:
        print("Gamas de datas encontradas:")
        for inicio, fim in gamas_de_datas:
            print(f"De {inicio} a {fim}")
    else:
        print("Nenhuma gama de datas encontrada no arquivo.")


#Número de ocorrências de #DATE:
def contar_ocorrencias_date(nome_arquivo):
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            conteudo = arquivo.read()
            count_date = conteudo.count("#DATE:")
            return count_date
    except FileNotFoundError:
        return "Arquivo não encontrado"
    except Exception as e:
        return f"Ocorreu um erro: {str(e)}"

if __name__ == "__main__":
    nome_arquivo = "folha8.OUT.txt"  

    total_ocorrencias_date = contar_ocorrencias_date(nome_arquivo)

    if isinstance(total_ocorrencias_date, int):
        print(f"O número total de ocorrências da expressão '#DATE:' é: {total_ocorrencias_date}")
    else:
        print(total_ocorrencias_date)


#5.Inventar alguma coisa para extrair do texto. Exercício livre
#Contar o número total de palavras

def contar_palavras(nome_arquivo):
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            conteudo = arquivo.read()
            palavras = conteudo.split()
            total_palavras = len(palavras)
            return total_palavras
    except FileNotFoundError:
        return "Arquivo não encontrado"
    except Exception as e:
        return f"Ocorreu um erro: {str(e)}"

if __name__ == "__main__":
    nome_arquivo = "folha8.OUT.txt"  

    total_palavras = contar_palavras(nome_arquivo)

    if isinstance(total_palavras, int):
        print(f"O número total de palavras no arquivo é: {total_palavras}")
    else:
        print(total_palavras)


#Calcular número total de cada pontuação

import re

def contar_pontuacoes(nome_arquivo):
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            conteudo = arquivo.read()
            padrao_pontuacao = r'[,\.;:!?]'
            matches = re.findall(padrao_pontuacao, conteudo)
            
            contagem_pontuacoes = {',': 0, ';': 0, ':': 0, '.': 0, '!': 0, '?': 0}

            for pontuacao in matches:
                contagem_pontuacoes[pontuacao] += 1

            return contagem_pontuacoes
    except FileNotFoundError:
        return "Arquivo não encontrado"
    except Exception as e:
        return f"Ocorreu um erro: {str(e)}"

if __name__ == "__main__":
    nome_arquivo = "folha8.OUT.txt"  

    contagem_pontuacoes = contar_pontuacoes(nome_arquivo)

    if isinstance(contagem_pontuacoes, dict):
        print("Contagem de pontuações:")
        for pontuacao, quantidade in contagem_pontuacoes.items():
            print(f"{pontuacao}: {quantidade}")
    else:
        print(contagem_pontuacoes)






