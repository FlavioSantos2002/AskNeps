numero_de_sorteios = int(input())

lista_de_valores = list(map(int, input().split()))

lista_de_listas = list()





    

def retornaLista(index, lista):
    if (index == len(lista)):
        index = index - 1
    l = list()
    l.append(lista[index])
    for v in range(len(lista) - index - 1):
        if (l[0] == lista[v + 1]):
            l.append(lista[v + 1])
    return l

    


print(retornaLista(0, lista_de_valores))
    

    




