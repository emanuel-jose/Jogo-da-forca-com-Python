import random, time, os

# função para "limpar" a tela do terminal
def limparTela():
    if os.name == 'ny': # verifica se o so é linux
        os.system('clear') # comando de limpar o terminal no linux
    else:
        os.system('cls') # comando de limpar o terminal no windows 

def enforcado(valor): # função para desenhar o boneco sendo enforcado. Recebe como parametro um valor inteiro
    forca = ['|','|','|','|','|','_','_','_','_','_','|'] # lista com as partes da forca
    partesDoCorpo = ['(_)','_/','|','\_','|','_/','\_'] # lista com as partes do corpo
    partesDoCorpoHide = [' ',' ',' ',' ',' ',' ',' '] # lista com as partes do corpo escondidas

    for i in range(0, valor): # contador que vai de 0 até o nº informado no parametro
        partesDoCorpoHide[i] = partesDoCorpo[i] # muda o valor escondido para a parte do corpo original seguindo o indice no contador

    # imprime as partes da forca com o boneco         
    print(f' {forca[5]}{forca[6]}{forca[7]}{forca[8]}{forca[9]}')
    print(f'{forca[4]}    {forca[10]}')
    print(f'{forca[3]}   {partesDoCorpoHide[0]}')
    print(f'{forca[2]}  {partesDoCorpoHide[1]}{partesDoCorpoHide[2]}{partesDoCorpoHide[3]}')
    print(f'{forca[1]}    {partesDoCorpoHide[4]}')
    print(f'{forca[0]}  {partesDoCorpoHide[5]} {partesDoCorpoHide[6]}')
    

# função para escolher uma palavra 
def escolheTitulo():
    listaDeTitulos = [] # lista que coterá as palavras digitadas pelo player
    print('Escolha três titulos:')
    while len(listaDeTitulos) < 3: # verifica se o espaço de três palavras já foi preenchido
        titulo = str(input('> ')).lower().strip() # input para inserir uma palavra na lista
        listaDeTitulos.append(titulo)
    global tituloEscolhido # var global que armazenara um tittulo sorteado
    tituloEscolhido = random.choice(listaDeTitulos)
    juntarLetras = '-'.join(tituloEscolhido) # junta as letras da palavra por '-'
    global letrasSeparadas # var global que separa a palavra letra a letra
    letrasSeparadas = juntarLetras.split('-')
    global PalavraSecreta # var global que que armazena a palavra sorteada escondida
    PalavraSecreta = []
    for letra in letrasSeparadas: # percorre a lista de letrasSeparada
        if letra != ' ': # se a casa em que a letra esta for diferente de um espaço, ou seja for uma letra msm
            letra = letra.replace(letra,'_') # troca o valor da letra por um '_'
        PalavraSecreta.append(letra) # e add a lista das Palavras Seceretas

# função para imprimir uma lista de letras como uma palavra
def imprimirPalavraSecreta(tituloSecreto): # o parametro sera uma lista de letras
    impressao = ''  # inicia uma var do tipo str
    for letra in tituloSecreto: # percorre a lista de letras
        impressao = impressao + " "+ letra # e atribui a var impressao as letras na lista
    print(impressao) # imprime na tela o resultado final

# função que imprime na tela as letras que já foram escolhidas pelo player
def imprimirLetrasEscolhida(lista): # o parametro é uma lista das letras
    mostrarLetras = '' # inicia uma var do tipo str
    for i in lista: # percorre a lista
        mostrarLetras = mostrarLetras + i + ',' # atribui a var mostrarLetras o conteudo da lista separando com ','
    print(f'letras já escolhidas: {mostrarLetras}') # imprime na tela o resultado final

# função do jogo
def inGame():
    escolheTitulo() # chama a função para escolha de uma palavra
    limparTela() # limpa a tela do terminal
    print('Escolhendo um titulo. Aguarde...')
    time.sleep(2) # mostra o print por 2s
    limparTela() # limpa a tela do terminal
    enforcado(0) # desenha a forca na tela
    imprimirPalavraSecreta(PalavraSecreta) # imprime a palavra com os '_' no lugar das letras

    letrasJaEscolhidas = [] # lista de letras já escolhidas pelo player
    vida = 7 # var que contara a vida do player, levando em consideração a (1) cabeça, (2) tronco, (3) quadril, (4) braço esquerdo, (5) braço direito, (6) perna esquerda, (7) perna direita
    aparecerBoneco = 0 # var que verificara o indice na lista de partes do corpo para poder desenhar o boneco na tela
    pontos = 0 # var que conta as letras acertivas
    quantRestante = PalavraSecreta.count('_') # conta quantas '_' tem na lista. Verificação que possibilita a verificação do nº de letras restantes para completar a palavra
    
    # laço que se repetira enquanto houver vida restante e letras restantes. Caso um dos dois for False o laço terminara
    while vida > 0 and quantRestante > 0:
        letraInformada = str(input('Esolha uma letra:\n> ')).lower().strip() # input para escolher uma letras
        if len(letraInformada) == 1: # verifica se o usuário digitou só um char
            if letraInformada not in letrasJaEscolhidas: # verifica se a letra que foi informada já se encontra na lista das escolhidas
                if letraInformada in letrasSeparadas: # verificar se a letra informada está na palavra sorteada
                    quant = letrasSeparadas.count(letraInformada) # conta quantas letras escolhidas há na palavra sorteada
                    pontos += 1 # add um ponto pela letra acertiva
                    if quant > 1: # se a quantidade de letras informada na palavra sorteada for maior que 1
                        while quant > 0: # enquanto a quantidade de letras for maior de 0. Verificação para conseguir percorrer a palavra inteira e encontrar suas posições
                            pos = letrasSeparadas.index(letraInformada) # acha a primeira posição da letra dentro da palavra sorteada
                            PalavraSecreta[pos] = letraInformada # muda o valor da letra na palavra secreta pegando por sua posição. Muda o valor '_' para a letra informada na posição correta
                            letrasSeparadas[pos] = "*" # muda o valor na lista de letras para que quando o laço retornar o primeiro indice corra ate outra casa. No caso faz com que seja possivel verificar as demais localidades dentro da lista da letra informada
                            quant = letrasSeparadas.count(letraInformada) # conta novamente no caso por conta do codigo acima diminui um
                        limparTela() # limpa a tela do terminal
                        
                    else: # caso haja somente uma letra informada na lista de letras
                        pos = letrasSeparadas.index(letraInformada) # verificar a 1º posição na lista
                        PalavraSecreta[pos] = letraInformada # muda o valor a partir da posição pela letra informada
                        limparTela() # limpa a tela do terminal
                else: # caso a letra informada não esteja na palavra
                    vida -= 1 # diminui um ponto na vida do player
                    aparecerBoneco += 1 # a cada vida descontada acrescenta uma parte do corpo quando for desenhar o boneco
                    limparTela() # limpa a tela do terminal
                letrasJaEscolhidas.append(letraInformada) # add a letra informada a lista de ja escolhidas. Para detectar se uma letra foi informada mais de uma vez.
            else: # caso a letra informada já esteja na lista de escolhidas, ou seja o user repetir a letra
                limparTela() # limpa a tela do terminal
                print('letra já escolhida!') # informa que a letra em questão já foi escolhida anteriormente
            
            enforcado(aparecerBoneco) # 
            imprimirPalavraSecreta(PalavraSecreta) # imprime a palvra secreta
            print(f'letras encontradas: {pontos}\nvida restante: {vida}') # imprime os dados do player
            imprimirLetrasEscolhida(letrasJaEscolhidas) # imprime as letras já escolhidas
        else: # caso o player tente digitar mais de uma letra
            print('Uma letra por vez!') # informa para ser digitado uma letra por vez
        quantRestante = PalavraSecreta.count('_') # verifica a quant de '_' na lista de PalavraSecreta
    if vida < 1: # se não houver mais vidas restantes
        limparTela() # limpa a tela do terminal
        enforcado(aparecerBoneco) # desenha a forca com as partes do boneco seguindo o parametro que conta quantas partes aparecera
        print(f'Você perdeu!\npalavra escolhida: {tituloEscolhido}\nletras encontradas: {pontos}\nvida restante: {vida}') # dados finais do player
    if quantRestante == 0: # se o player tiver completado a palavra
        limparTela() # limpa a tela do terminal
        print(f'Você venceu!\npalavra escolhida: {tituloEscolhido}\nletras encontradas: {pontos}\nvida restante: {vida}') # dados finais do player


inGame() # chama a função para iniciar o jogo
