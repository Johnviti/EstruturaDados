from Miniprojeto import eh_possivel_sair
from labirinto import gera_lab

labirinto2 = [
    ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
    [' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', '#'],
    ['#', '#', ' ', ' ', ' ', '#', '#', ' ', '#', '#'],
    ['#', ' ', ' ', '#', '#', '#', '#', ' ', '#', ' '],
    ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#']
]

resultado = eh_possivel_sair(labirinto2)

print(resultado)

labirinto1 = [

['#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
[' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', '#'],
['#', ' ', ' ', ' ', '#', '#', ' ', ' ', ' ', '#'],
['#', '#', '#', ' ', ' ', '#', ' ', ' ', '#', '#'],
['#', '#', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' '],
['#', '#', '#', '#', '#', '#', '#', '#', '#', '#']]

resultado1 = eh_possivel_sair(labirinto1)

print(resultado1)

labirinto = gera_lab()

print(labirinto)

resultadoTeste = eh_possivel_sair(labirinto)

print(resultadoTeste)