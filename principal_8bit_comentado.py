import pygame
from pygame.locals import *
from time import *
from random import randint
from random import choice
import sys
red=(255,0,0)

#----------------------------- Funciones -------------------------------------#

#Funcion que genera una matriz con 0 y luego agrega valores aleatorios desde la mitad hacia abajo.
def generar_matriz():
    i=0
    M=[]
    while i<15:
        j=0
        L=[]
        while j<17:
            L=L+[0]
            j+=1
        M=M+[L]
        i+=1
    j=0
    while j<17:
        i=7
        num_bolas=randint(0,6)
        i=i+num_bolas
        while i<15:
            M[i][j]=randint(1,5)
            i+=1
        j+=1
    return M

#Funcion que imprime la matriz por consola, para fines desbug
def imprime_matriz(M):
    for fila in M:
        print fila


#Funcion que analiza el color en la posicion xpos, ypos y carga la bola correspondiente en pantalla.
def analizar_color(actual,xpos,ypos):
    if actual==1:
        azul=pygame.image.load('azul.png')
        pantalla.blit(azul,(xpos,ypos))
    if actual==2:
        rojo=pygame.image.load('red.png')
        pantalla.blit(rojo,(xpos,ypos))
    if actual==3:
        mor=pygame.image.load('purple.png')
        pantalla.blit(mor,(xpos,ypos))
    if actual==4:
        verde=pygame.image.load('verde.png')
        pantalla.blit(verde,(xpos,ypos))
    if actual==5:
        yellow=pygame.image.load('yellow.png')
        pantalla.blit(yellow,(xpos,ypos))

#Funcion que recorre matriz y fija las posiciones para cargar las bolas llamando a analizar_color.
def llenar_balls(M):   
    j=0
    while j<17:
        i=0
        while i<15:
            xpos=(39*j)+40
            ypos=(39*i)+50
            analizar_color(M[i][j],xpos,ypos)
            i+=1
        j+=1

#Funcion que transpone una matriz para analizar filas mejor.        
def transpuesta(matriz):
        filas= len(matriz)
        columnas= len(matriz[0])
        return [[matriz[j][i] for j in xrange(filas)] for i in xrange(columnas)]

#Funcion que permite agregar una pelota cuando el usuario juega, de la misma forma revienta las pelotas del mismo color.    
def agregar_ball(M,j,sgteball):
    i=14
    flag=0
    while flag==0 and i>=0 and j>=0:
        if M[i][j]==0:
            M[i][j]=sgteball
            xpos=(39*j)+40
            ypos=(39*i)+50
            analizar_color(M[i][j],xpos,ypos)
            pygame.display.update()
            flag=1
            pygame.time.delay(100)
            M1=transpuesta(M)
            M1,deli,delj=explotar(j,i,sgteball,0,M1,[],[])
            if len(deli)>2:
                M=gravedad(M1,deli,delj)
        i-=1
    return M

#Funcion principal desde el momento que se comienza a jugar hasta que se gana, se pierde o se decide salir del juego.
def jugar(M):
    fin=False
    plays=0
    sgteball=randint(1,5)
    analizar_color(sgteball,752,520)
    while not fin:
        for evento in pygame.event.get():
            if evento.type==pygame.QUIT:
                fin=True
                pygame.quit()
                sys.exit(0)
            if evento.type==pygame.MOUSEBUTTONDOWN:
                xpos1,ypos1=pygame.mouse.get_pos()
                if rect1_game.collidepoint(xpos1,ypos1) and M[0][0]==0:
                    plays+=1
                    j=0
                elif rect2_game.collidepoint(xpos1,ypos1)and M[0][1]==0:
                    plays+=1
                    j=1
                elif rect3_game.collidepoint(xpos1,ypos1)and M[0][2]==0:
                    plays+=1
                    j=2
                elif rect4_game.collidepoint(xpos1,ypos1)and M[0][3]==0:
                    plays+=1
                    j=3
                elif rect5_game.collidepoint(xpos1,ypos1)and M[0][4]==0:
                    plays+=1
                    j=4
                elif rect6_game.collidepoint(xpos1,ypos1)and M[0][5]==0:
                    plays+=1
                    j=5
                elif rect7_game.collidepoint(xpos1,ypos1)and M[0][6]==0:
                    plays+=1
                    j=6
                elif rect8_game.collidepoint(xpos1,ypos1)and M[0][7]==0:
                    plays+=1
                    j=7
                elif rect9_game.collidepoint(xpos1,ypos1)and M[0][8]==0:
                    plays+=1
                    j=8
                elif rect10_game.collidepoint(xpos1,ypos1)and M[0][9]==0:
                    plays+=1
                    j=9
                elif rect11_game.collidepoint(xpos1,ypos1)and M[0][10]==0:
                    plays+=1
                    j=10
                elif rect12_game.collidepoint(xpos1,ypos1)and M[0][11]==0:
                    plays+=1
                    j=11
                elif rect13_game.collidepoint(xpos1,ypos1)and M[0][12]==0:
                    plays+=1
                    j=12
                elif rect14_game.collidepoint(xpos1,ypos1)and M[0][13]==0:
                    plays+=1
                    j=13
                elif rect15_game.collidepoint(xpos1,ypos1)and M[0][14]==0:
                    plays+=1
                    j=14
                elif rect16_game.collidepoint(xpos1,ypos1)and M[0][15]==0:
                    plays+=1
                    j=15
                elif rect17_game.collidepoint(xpos1,ypos1)and M[0][16]==0:
                    plays+=1
                    j=16
                else:
                    if circ_restart.collidepoint(xpos1,ypos1):
                        pantalla.blit(fondo_game,(0,0))
                        M=generar_matriz()
                        llenar_balls(M)
                        M=jugar(M)
                        fin=True
                        return M
                    elif circ_menu.collidepoint(xpos1,ypos1):
                        pantalla.blit(menu,(0,0))
                        M=generar_matriz()
                        return M
                    elif circ_exit.collidepoint(xpos1,ypos1):
                        pantalla.blit(game_over,(0,0))
                        pygame.display.update()
                        pygame.time.delay(1000)
                        pygame.quit()
                        sys.exit(0)
                    j=-1
                    
                M=agregar_ball(M,j,sgteball)
                fin,win=verificar(M)
                sgteball=sgteballvalida(M)
                if plays==15:
                    M=agregar_fila(transpuesta(M))
                    llenar_balls(M)
                    plays=0
                    fin,win=verificar(M)
                if j>=0:
                    pantalla.blit(fondo_game,(0,0))
                    analizar_color(sgteball,752,520)
                    llenar_balls(M)
                if fin and win:
                    pantalla.blit(you_win,(0,0))
                    pygame.display.update()
                    pygame.time.delay(2000)
                    pantalla.blit(menu,(0,0))
                    M=generar_matriz()
                    return M
                if fin and not win:
                    pantalla.blit(game_over,(0,0))
                    pygame.display.update()
                    pygame.time.delay(2000)
                    pantalla.blit(menu,(0,0))
                    M=generar_matriz()
                    return M
        pygame.display.update()

#Funcion que verifica si el usuario gano o perdio en base a las bolas en la matriz.
def verificar(M):
    i=14
    j=0
    aux=0
    perder=False
    while j<17:
        if M[i][j]==0:
            aux+=1
        j+=1
    i=0
    j=0
    while j<17:
        if M[i][j]!=0:
            perder=True
        j+=1
    if aux==17:
        return True,True
    elif perder:
        return True,False
    else:
        return False,False

#Funcion que cada x pelotas agregadas, agrega una fila extra como modo de dificultad
def agregar_fila(M):
    i=0
    while i<len(M):
        M[i].insert(len(M)-1,randint(1,5))
        del M[i][0]
        i+=1
    return transpuesta(M)

#Funcion que valida posiciones en matriz.
def validar_pos(i,j,ball,M):
    if i>=0 and i<len(M) and j>=0 and j<len(M[i]):
        if M[i][j]==ball:
            return True

#Funcion de BACKTRAKING que explota las pelotas del mismo color y aplica gravedad a toda la matriz.    
def explotar(i,j,ball,aux,M,deli,delj):
    a=[1,0,-1,0]
    b=[0,1,0,-1]
    k=0
    deli.append(i)
    delj.append(j)
    M[i][j]=0
    while k<4:
        if validar_pos(i+a[k],j+b[k],ball,M):
            aux+=1
            explotar(i+a[k],j+b[k],ball,aux,M,deli,delj)
        k+=1
    if aux==0:
        M[i][j]=ball
        return M,[],[]
    else:
        return M,deli,delj

#Funcion que simula la gravedad y permite que las pelotas que queden en el aire caigan. 
def gravedad(M,deli,delj):
    if len(deli)!=0:
        fin=False
    else:
        fin=True
    while not fin:
        aux=[]
        aux2=[]
        k=0
        actual=deli[k]
        while k<len(deli):          
            if actual==deli[k]:
                aux.append(deli[k])
                aux2.append(delj[k])
                del deli[k]
                del delj[k]
            else:
                k+=1
        aux.sort()
        aux2.sort()
        l=0
        while l<len(aux):
            del M[aux[l]][aux2[l]]
            M[aux[l]].insert(0,0)
            l+=1
        if len(deli)==0:
            fin=True
    return transpuesta(M)

def sgteballvalida(M):
    lista=[]
    i=0
    while i<len(M):
        j=0
        while j<len(M[i]):
            if M[i][j]!=0:
                lista.append(M[i][j])
            j+=1
        i+=1
    i=0
    lista1=[]
    while len(lista)!=0:
        i=0
        aux=lista[i]
        lista1.append(aux)
        while i<len(lista):
            if lista[i]==aux:
                del lista[i]
            else:
                i+=1
    if len(lista1)>0:
        return choice(lista1)
    else:
        return 0
            
    
#------------------------------ Programa Principal -----------------------------------#

pygame.init()
pantalla=pygame.display.set_mode((830,664))
pygame.display.set_caption('Coball')        
menu=pygame.image.load('menu1.jpg')
fondo_game=pygame.image.load('fondo_game1.jpg')
game_over=pygame.image.load('game_over.png')
you_win=pygame.image.load('you_win.png')
rect1_menu=pygame.draw.rect(pantalla,red,(345,380,150,45),0)
rect2_menu=pygame.draw.rect(pantalla,red,(355,490,130,42),0)
rect1_game=pygame.draw.rect(pantalla,red,(30,30,49,615),0)
rect2_game=pygame.draw.rect(pantalla,red,(79,30,39,615),0)
rect3_game=pygame.draw.rect(pantalla,red,(118,30,39,615),0)
rect4_game=pygame.draw.rect(pantalla,red,(157,30,39,615),0)
rect5_game=pygame.draw.rect(pantalla,red,(196,30,39,615),0)
rect6_game=pygame.draw.rect(pantalla,red,(235,30,39,615),0)
rect7_game=pygame.draw.rect(pantalla,red,(274,30,39,615),0)
rect8_game=pygame.draw.rect(pantalla,red,(313,30,39,615),0)
rect9_game=pygame.draw.rect(pantalla,red,(352,30,39,615),0)
rect10_game=pygame.draw.rect(pantalla,red,(391,30,39,615),0)
rect11_game=pygame.draw.rect(pantalla,red,(430,30,39,615),0)
rect12_game=pygame.draw.rect(pantalla,red,(469,30,39,615),0)
rect13_game=pygame.draw.rect(pantalla,red,(508,30,39,615),0)
rect14_game=pygame.draw.rect(pantalla,red,(547,30,39,615),0)
rect15_game=pygame.draw.rect(pantalla,red,(586,30,39,615),0)
rect16_game=pygame.draw.rect(pantalla,red,(625,30,39,615),0)
rect17_game=pygame.draw.rect(pantalla,red,(664,30,46,615),0)
circ_menu=pygame.draw.circle(pantalla,red,(770,68),46,0)
circ_restart=pygame.draw.circle(pantalla,red,(773,173),47,0)
circ_exit=pygame.draw.circle(pantalla,red,(773,280),47,0)
pantalla.blit(menu,(0,0))
M=generar_matriz()
fin= False
#Ciclo infinito desde que se inicia el juego hasta que se cierra.
while not fin:
    for evento in pygame.event.get():
        if evento.type==pygame.QUIT:
            fin=True
        elif evento.type==pygame.MOUSEBUTTONDOWN:
            xpos,ypos=pygame.mouse.get_pos()
            if rect1_menu.collidepoint(xpos,ypos):
                pantalla.blit(fondo_game,(0,0))
                llenar_balls(M)
                M=jugar(M)
            if rect2_menu.collidepoint(xpos,ypos):
                fin=True
    pygame.display.update()
pygame.quit()
    
    
