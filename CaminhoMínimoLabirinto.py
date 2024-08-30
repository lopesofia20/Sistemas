from collections import deque

def caminho(labirinto):
    if not labirinto or not labirinto[0]:
        return -1
    
    n = len(labirinto)
    m = len(labirinto[0])
    
    if labirinto[0][0] == 1 or labirinto[n-1][m-1] == 1:
        return -1
    
    direcoes = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    fila = deque([(0, 0, 1)])
    
    labirinto[0][0] = 1
    
    while fila:
        x, y, dist = fila.popleft()
        
        if x == n-1 and y == m-1:
            return dist
        
        for dx, dy in direcoes:
            novo_x, novo_y = x + dx, y + dy
            
            if 0 <= novo_x < n and 0 <= novo_y < m and labirinto[novo_x][novo_y] == 0:
                fila.append((novo_x, novo_y, dist + 1))
                labirinto[novo_x][novo_y] = 1

    return -1


labirinto = [
    [0, 1, 0, 0],
    [0, 0, 0, 1],
    [1, 0, 1, 0],
    [0, 0, 0, 0]
]
print(caminho(labirinto))
