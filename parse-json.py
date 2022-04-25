import sys
import string
import json

lista_livros = []
dic_livros = {}

def monta_lista():
    with open('/home/user/Documents/script/json/json_Complexo.json') as json_file:
        jsondata = json.load(json_file)
        for i in jsondata:
            for k in jsondata[i]:
                if('prateleira' in k):
                    for p in jsondata[i][k]:
                        lista_livros.append(p['titulo'])

def dicionario_livros():
    with open('/home/user/Documents/script/json/json_Complexo.json') as json_file:
        jsondata = json.load(json_file)
        for i in jsondata:
            for k in jsondata[i]:
                if('prateleira' in k):
                    for p in jsondata[i][k]:
                        dic_livros['prateleira'] = k
                        dic_livros['livro'] = p['titulo']
                        print(dic_livros)

def mostra_lista():
    print(lista_livros)

def listar_ativos():
    with open('/home/user/Documents/script/json/json_Complexo.json') as json_file:
        jsondata = json.load(json_file)
        for i in jsondata: 
            if(i == 'clientes'):
                for k in jsondata[i]:
                    if(jsondata[i][k]['ativo'] == 'true'):
                        print(k)


def main():
    #monta_lista()
    #mostra_lista()
    dicionario_livros()
    listar_ativos()

if __name__ =='__main__':
    main()