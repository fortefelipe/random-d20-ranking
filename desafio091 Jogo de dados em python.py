from random import randint
from time import sleep
#pra ordenar o dicionário, usar itemgetter
from operator import itemgetter
jogadores = []
for cont in range(1, 6):
        jogadores.append(str(input(f'Digite o nome para o Jogador {cont}: ')))
jogo = {(jogadores[0]): randint(1, 20),
        (jogadores[1]): randint(1, 20),
        (jogadores[2]): randint(1, 20),
        (jogadores[3]): randint(1, 20),
        (jogadores[4]): randint(1, 20)
        }
ranking = []
print('Resultados: ')
for k, v in jogo.items():
        print(f'{k} rolou {v}.')
        sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True) #reverse serve para ordenar do maior para o menor.
print('-=' * 20)
print(' == RESULTADO == ')
for i, v, in enumerate(ranking):
        print (f'   {i+1}º lugar: {v[0]} com {v[1]}.')
        sleep(1)
        