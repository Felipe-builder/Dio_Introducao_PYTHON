import shutil


def escrever_arquivo(nome_arquivo, texto):
    # diretorio = '/home/felipe/Documents/python/teste.txt'
    arquivo = open(nome_arquivo, 'w')
    arquivo.write(texto)
    arquivo.close()


def atualizar_arquivo(nome_arquivo, texto):
    arquivo = open(nome_arquivo, 'a')
    if type(texto) == list:
        for li in texto:
            for k, v in li.items():
                arquivo.write(f'O aluno {k} está com a média {v}.\n')
    elif type(texto) == str:
        arquivo.write(texto)
    arquivo.close()


def ler_arquivo(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    texto_nota = arquivo.read()
    print(texto_nota)


def media_notas(nomes_arquivo):
    arquivo = open(nomes_arquivo, 'r')
    aluno_nota = arquivo.read()
    # print(aluno_nota)
    aluno_nota = aluno_nota.split('\n')
    # print(aluno_nota)
    lista_media = []
    for linha in aluno_nota:
        lista_notas = linha.split(',')
        aluno = lista_notas[0]
        lista_notas.pop(0)
        print(aluno)
        print(lista_notas)
        media = lambda notas: sum([int(i) for i in notas]) / 4
        print(media(lista_notas))
        lista_media.append({aluno: media(lista_notas)})
    return lista_media


def copia_arquivo(nome_arquivo):
    shutil.copy(nome_arquivo, '/home/felipe/Documents/python/')


def move_arquivo(nome_arquivo):
    shutil.move(nome_arquivo, '/home/felipe/Documents/python/')


if __name__ == '__main__':
    # copia_arquivo('notas.txt')
    move_arquivo('notas.txt')
    # lista_media = media_notas('notas.txt')
    # print(lista_media)
    # escrever_arquivo('medias.txt', 'MÉDIAS DOS ALUNOS\n')
    # atualizar_arquivo('medias.txt', lista_media)
    # escrever_arquivo('Primeira linha.\n')
    # atualizar_arquivo('Segunda linha.\n')
    # aluno = 'Cesar, 7, 9, 3, 8\n'
    # atualizar_arquivo('notas.txt', aluno)
    # ler_arquivo('teste.txt')
    # ler_arquivo('notas.txt')
