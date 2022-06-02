class Grafo:

    def __init__(self, vertices):
        self.vertices = vertices
        self.grafo = [[0]*self.vertices for i in range(self.vertices)]
        self.alfabeto = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S']
        self.grau = 0
        self.atual = ''
        self.num_atual = 0
        self.ant = ''
        self.num_ant = 0
        self.percorridos = []
        self.entrada = ''
        self.saida = ''

    def adiciona_aresta(self, partida, destino, mostrar=True):
        partida = partida
        destino = destino
        p = ord(partida) - 64
        d = ord(destino) - 64
        
        self.grafo[p-1][d-1] = self.grafo[p-1][d-1]+1

        if(p != d):
            self.grafo[d-1][p-1] = self.grafo[d-1][p-1]+1

        if(mostrar):
            print(f'Porta adiciona entre as salas {partida} - {destino}')

    def mostra_matriz(self):
        print('A matriz de adjacência é:')
        print('__|__A__B__C__D__E__F__G__H__I__J__K__L__M__N__O__P__Q__R__S|')
        j = 0
        for i in range(self.vertices):
            print(f'{self.alfabeto[j]} | {self.grafo[i]}')
            j+=1

    def fecha_porta(self, partida, destino):
        partida = partida
        destino = destino
        p = ord(partida) - 64
        d = ord(destino) - 64

        if(self.grafo[p-1][d-1] != 0 and self.grafo[d-1][p-1] != 0):
            self.grafo[p-1][d-1] = self.grafo[p-1][d-1]-1
            if(p != d):
                self.grafo[d-1][p-1] = self.grafo[d-1][p-1]-1

    def tem_aresta(self, partida, destino):
        partida = partida
        destino = destino
        p = ord(partida) - 64
        d = ord(destino) - 64

        if(self.grafo[p-1][d-1] == 0):
            return False
        else:
            return True

    def grau_sala(self, sala, entrada, saida):
        sala = sala
        p = ord(sala) - 64

        self.grau = 0

        if(self.entrada == sala):
            self.grau += 1
        if(self.saida == sala):
            self.grau += 1

        for i in range(len(self.grafo[p-1])):
            if(i == p-1 and self.grafo[p-1][i] != 0):
                print(f'p-1: {p-1}')
                self.grau = self.grau + 2
            else:
                self.grau += self.grafo[p-1][i]
        
        return self.grau

    def percorre_sala(self, entrada, saida, fechada):

        if(not fechada):
            self.adiciona_portas(entrada, saida)
            print(" ")
            print("Percorrendo planta modificada...")
        else:
            print("Percorrendo planta fechada...")

        self.percorridos.clear()

        entrada = entrada
        saida = saida
        e = ord(entrada) - 64
        s = ord(saida) - 64

        self.atual = entrada
        num_atual = e
        self.num_atual = num_atual

        self.ant = entrada
        num_ant = e
        self.num_ant = num_ant

        self.percorridos.append(self.atual)

        while(self.atual != saida):
            
            num_atual = ord(self.atual) - 64
            self.num_atual = num_atual
            i = 0
            for i in range(len(self.grafo[self.num_atual-1])):
                print(f'Sala atual: {self.atual} - Porta com sala {chr(i+65)} ? {self.grafo[self.num_atual-1][i]}')
                if(self.grafo[self.num_atual-1][i] != 0):
                    self.num_ant = self.num_atual
                    self.num_atual = i+1

                    self.ant = chr(self.num_ant+64)
                    self.atual = chr(self.num_atual+64)
                    print(f'{self.ant} -> {self.atual}')

                    self.percorridos.append(self.atual)
                    self.fecha_porta(self.ant, self.atual)
                    if(self.atual == saida): break
        

        print(f'Salas percorridas: {self.percorridos}')

    def adiciona_portas(self, entrada, saida):
        self.entrada = entrada
        self.saida = saida

        indice = 1

        for i in self.percorridos:

            if(self.grau_sala(i, entrada, saida) % 2 != 0):
                self.adiciona_aresta(i, self.percorridos[indice])

            indice += 1
        
        print(' ')
        print('============== MATRIZ COM PORTAS ADICIONADAS ==============')
        print(' ')

        self.mostra_matriz()

        print(' ')
        print('============== TABELA COM PORTAS ADICIONADAS ==============')
        print(' ')

        self.tabela_grafo()

    def tabela_grafo(self):
        print(f'|_SALA__|_SALA__|_PORTAS_|')
        for i in range(len(self.grafo)):
            for j in range(i):
                if(self.grafo[i][j] != 0):
                    if(self.grafo[i][j] > 9):
                        print(f'|   {chr(i+65)}   |   {chr(j+65)}   |   {self.grafo[i][j]}   |')
                    else:
                        print(f'|   {chr(i+65)}   |   {chr(j+65)}   |   {self.grafo[i][j]}    |')

    def remove_portas(self):
        for i in range(19):
            for j in range(19):
                self.grafo[i][j] = 0

def construir_salas_fechadas(g):
    # -------- A ----------
    g.adiciona_aresta('A','B', False)
    g.adiciona_aresta('A','C', False)

    # -------- B ----------
    g.adiciona_aresta('B','J', False)

    # -------- C ----------
    g.adiciona_aresta('C','D', False)

    # -------- D ----------
    g.adiciona_aresta('D','E', False)
    g.adiciona_aresta('D','J', False)
    g.adiciona_aresta('D','I', False)

    # -------- E ----------
    g.adiciona_aresta('E','F', False)

    # -------- F ----------
    g.adiciona_aresta('F','G', False)

    # -------- G ----------
    g.adiciona_aresta('G','H', False)

    # -------- H ----------
    g.adiciona_aresta('H','I', False)

    # -------- I ----------
    g.adiciona_aresta('I','J', False)
    g.adiciona_aresta('I','R', False)

    # -------- J ----------
    g.adiciona_aresta('J','K', False)
    g.adiciona_aresta('J','O', False)
    g.adiciona_aresta('J','P', False)

    # -------- K ----------
    g.adiciona_aresta('K','L', False)

    # -------- L ----------
    g.adiciona_aresta('L','M', False)

    # -------- M ----------
    g.adiciona_aresta('M','N', False)

    # -------- N ----------
    g.adiciona_aresta('N','O', False)
    g.adiciona_aresta('N','Q', False)
    g.adiciona_aresta('N','Q', False)

    # -------- O ----------
    g.adiciona_aresta('O','P', False)
    g.adiciona_aresta('O','P', False)

    # -------- P ----------
    g.adiciona_aresta('P','Q', False)
    g.adiciona_aresta('P','R', False)
    g.adiciona_aresta('P','R', False)

    # -------- Q ----------
    g.adiciona_aresta('Q','S', False)

    # -------- R ----------
    g.adiciona_aresta('R','S', False)
    g.adiciona_aresta('R','S', False)
    g.adiciona_aresta('R','S', False)

def remove_portas(g):
    for i in range(19):
        for j in range(19):
            g[i][j] = 0

g = Grafo(19)

while(True):
    entrada = input('Sala de entrada: ')
    saida = input('Sala de saída: ')
    entrada = entrada.upper()
    saida = saida.upper()
    # print(ord(entra
    if(len(entrada) == 1 and len(saida) == 1 and (ord(entrada) - 64) < 20 and (ord(saida) - 64) < 20):
        break
    else:
        print('Digite opções válidas.')

construir_salas_fechadas(g)

print(' ')
print('============== MATRIZ DA SALA FECHADA ==============')
print(' ')

g.mostra_matriz()

print(' ')
print('============== TABELA DA SALA FECHADA ==============')
print(' ')

g.tabela_grafo()

print(' ')
print('============== PERCORRENDO A SALA FECHADA PARA OBTENÇÃO DO VETOR COM O CAMINHO ==============')
print(' ')

g.percorre_sala(f'{entrada}', f'{saida}', True)

g.remove_portas()

construir_salas_fechadas(g)
print(' ')
print('============== PERCORRENDO A SALA ABERTA E ADICIONANDO PORTAS NECESSÁRIAS ==============')
print(' ')

g.percorre_sala(f'{entrada}', f'{saida}', False)

print(' ')
print('============== MATRIZ DA SALA ABERTA PÓS PERCORRIDA ==============')
print(' ')

g.mostra_matriz()

print(' ')
print('============== TABELA DA SALA ABERTA PÓS PERCORRIDA ==============')
print(' ')

g.tabela_grafo()

print(' ')
print('=================================')
print('A SALA DE ESPELHOS É SEGURA.')
print('=================================')
print(' ')