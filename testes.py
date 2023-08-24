from Miniprojeto import eh_possivel_sair, mostrar
from labirinto import gera_lab

#Teste 1
labirinto1 = [

['#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
[' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', '#'],
['#', ' ', ' ', ' ', '#', '#', ' ', ' ', ' ', '#'],
['#', '#', '#', ' ', ' ', '#', ' ', ' ', '#', '#'],
['#', '#', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' '],
['#', '#', '#', '#', '#', '#', '#', '#', '#', '#']]

resultado_esperado1 = True
resultado1 = eh_possivel_sair(labirinto1)
print(resultado1 == resultado_esperado1) #deve ser True

if resultado1:
    print("Conseguimos achar uma saída: " + mostrar(labirinto1)) #é pra printar com o 'X' na casa (9,4)

#Teste 2
labirinto2 = [['#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
[' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', '#'],
['#', '#', ' ', ' ', ' ', '#', '#', ' ', '#', '#'],
['#', ' ', ' ', '#', '#', '#', '#', ' ', '#', ' '],
['#', '#', '#', '#', '#', '#', '#', '#', '#', '#']]

resultado_esperado1 = False
resultado1 = eh_possivel_sair(labirinto2)
print(resultado1 == resultado_esperado1) #deve ser True

if resultado1:
    print(mostrar(labirinto2))


labirinto = gera_lab(7,15) #gerando um labirinto
print(labirinto)
resultadoTeste = eh_possivel_sair(labirinto)
print(resultadoTeste)