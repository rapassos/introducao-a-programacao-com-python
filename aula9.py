###############################################
# Author: Rafael Passos Guimarães
# E-mail: rapassos@gmail.com
# Date: 12/Jul/2020
###############################################

import shutil

# Manipulação de arquivos
def arquivo_escrever(nomeArquivo, texto):
    arquivo = open('teste.txt','w')
    arquivo.write(texto)
    arquivo.close()

def arquivo_atualizar(nomeArquivo, texto):
    arquivo = open(nomeArquivo,'a')
    arquivo.write(texto)
    arquivo.close()

def arquivo_ler(nomeArquivo):
    arquivo = open(nomeArquivo,'r')
    texto = arquivo.read()
    print(texto)

media = lambda notas: sum([float(i) for i in notas])/4

def mediaNotas(nomeArquivo):
    arquivo = open(nomeArquivo,'r')
    alunoNotas = arquivo.read()
    for linha in alunoNotas.split('\n'):
        aluno = linha.split(',')
        nomeAluno = aluno.pop(0)
        if nomeAluno != '':
            print('A média do aluno {} é: {}'.format(nomeAluno,media(aluno)))
    arquivo.close()
        

def copiaArquivo(nomeArquivo):
    shutil.copy(nomeArquivo,'./teste/notas_copy.txt')

def moveArquivo(nomeArquivo):
    shutil.move(nomeArquivo,'./notas_move.txt')

if __name__ == "__main__":
    pass
    # arquivo_escrever('teste.txt','Primeira linha.\n')
    # arquivo_atualizar('teste.txt','Segunda linha.\n')
    # arquivo_atualizar('teste.txt','Terceira linha.\n')
    # arquivo_ler('teste.txt')

    #aluno = 'Lucas,7,3,6,9.5'
    #arquivo_atualizar('notas.txt','{}\n'.format(aluno))
    #mediaNotas('notas.txt')
    
    #copiaArquivo('notas.txt')
    #moveArquivo('./teste/notas_copy.txt')

