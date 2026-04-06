# Operacoes com arquivos e diretorios em Python:
#Algoritmo Op_ArqMod-Ex38-02.

import os

#Declarar variaveis globais:
linha : str = ''
dir: str = ''
arq : str = ''
txt : str = ''

#Inicio

def main():
    #Variaveis globais:
    global linha
    global dir
    global arq

    dir = '/tmp/exercicios/'
    arq = 'ex38.txt'

    le_conteudo(dir, arq)
    
#FIM.

def le_conteudo(dir, arq):
    valor : int = 0
    cont : int = 0
    ims : str = ''
    num : str = ''
    linha : str = ''
    arquivo : str = ''
    registro : str = ''

    arquivo = dir + arq


    if (os.path.exists(dir) and os.path.isdir(dir)):
        
        with open (arquivo) as file:                    # abre o arquivo como uma string, linha por linha
            for linha in file:                          # para o conteudo de cada linha de file, ele deposita na variavel chamada "linha"     

                linha = linha.strip()
                if not (('Maior' in linha) or ('Menor' in linha)):

                    if(linha==''):
                        continue
                    else:
                        valor = int(linha)
                
                    if valor % 5 == 0:
                        print (valor, 'divisivel por 5.')
                        registro = str(valor) + ' divisivel por 5.'+'\n'
                        cont += 1
                
                    else:
                        print (valor, 'nao divisivel por 5.')
                        registro = str(valor) + ' nao divisivel por 5.'+'\n'
                        cont += 1

                    escreveArq(registro, cont)

#Fim-segue.

def escreveArq(linha, cont):
    #Variaveis grobais:
    dir01 : str = ''
    arq01 : str = ''
    global txt

    dir01 = '/tmp/exercicios/'
    arq01 = 'ex38-02.txt'

    #Variaveis locais:
    file: str = ''
    tipo: str = ''
    enc: str = ''
    
    if not (os.path.exists(dir01)):
        #Criando o diretorio.
        os.mkdir(dir)
        os.makedirs(dir, exist_ok = True)
        os.chmod(dir, 0o744) #Autorizacao de criacao, leitura e alteracao para o primeiro usuario, leitura para os demais.

    if (os.path.exists(dir) and os.path.isdir(dir)):
        tipo = 'w'
        txt = dir01 + arq01
        enc = 'utf-8'

        if (os.path.exists(txt)) and (cont != 1):
            tipo = 'a'
       
        with open (txt, tipo, encoding=enc) as file:
            file.write(linha)
    
    else:
        print("Diretorio invalido")
    
    #Fim-se.
#Fim-segue.

if __name__ == "__main__" :
    main()
#Fim-se.

