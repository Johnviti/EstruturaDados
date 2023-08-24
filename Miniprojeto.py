from labirinto import gera_lab, print_lab
from Stack import *

def eh_possivel_sair(labirinto):
    def esta_vazio(x, y):
        return 0 <= x < len(labirinto) and 0 <= y < len(labirinto[0]) and labirinto[x][y] == ' '
    
    stack = Stack()  
    stack.push((0, 0)) 
    percorrido = []
    
    while not stack.is_empty():
        x, y = stack.top()
        
        saida = (len(labirinto) - 2, len(labirinto[0]) - 1) #(m - 2, n - 1)

        if (x, y) in percorrido:
            stack.pop()
            percorrido.pop()
            continue
        
        percorrido.append((x, y))
        
        if (x, y) == saida:
            labirinto[x][y] = 'x'  
            return True  
        
        labirinto[x][y] = '+'  

        #imprimi o labirinto
        for linhas in labirinto:
            print(''.join(linhas))
        print()
        
        opcoes = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        proxima_opcao = None
        
        for campoX, campoY in opcoes:
            novo_x, novo_y = x + campoX, y + campoY
            
            if esta_vazio(novo_x, novo_y)and (novo_x, novo_y) not in percorrido:
                proxima_opcao = (novo_x, novo_y)
                break
            if
            
        if proxima_opcao:
            stack.push(proxima_opcao)
        else:
            stack.pop()
            percorrido.pop()    
        

    return False  # Não foi encontrada uma saída

def mostrar(labirinto):
    for linhas in labirinto:
        print(''.join(linhas))
