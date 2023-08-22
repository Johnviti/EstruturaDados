from labirinto import gera_lab, print_lab
from Stack import *

def eh_possivel_sair(labirinto):
    def esta_vazio(x, y):
        return 0 <= x < len(labirinto) and 0 <= y < len(labirinto[0]) and labirinto[x][y] == ' '
    
    stack = Stack()  # Usando a classe Stack
    stack.push((0, 0))  # Início do labirintoirinto
    percorrido = set()
    
    while not stack.is_empty():
        x, y = stack.pop()
        saida = (len(labirinto) - 2, len(labirinto[0]) - 1) #(m - 2, n - 1)

        if (x, y) in percorrido:
            continue
        
        percorrido.add((x, y))
        
        if (x, y) == saida:
            return True  
        
        labirinto[x][y] = '+'  

        # Mostra o labirintoirinto com os passos atuais
        # for linhas in labirinto:
        #     print(''.join(linhas))
        # print()
        
        opcoes = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        for dx, dy in opcoes:
            new_x, new_y = x + dx, y + dy
            
            if esta_vazio(new_x, new_y):
                stack.push((new_x, new_y))
    
    return False  # Não foi encontrada uma saída

