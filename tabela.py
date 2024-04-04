import pandas as pd

def imprimir_tabela_cvs ( caminho_aquivo ):
    try:
        dados = pd . read_csv ( caminho_arquivo )
        
        print ( dados )
    except FileNotFoundError:
        print ( "Arquivo não encontrado." )
    except Exception as e:
        print ( "Ocorreu um erro:" , e )
        
if __name__ == "__main__" :
    caminho_arquivo = input ( "Digite o caminho completo do arquivo CSV:" )
imprimir_tabela_cvs ( caminho_arquivo )