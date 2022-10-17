from doctest import master
import os
import math
import time
import random
from typing import final
import keyboard


masterlist = []
splittedlist = []
idlist = []
contadorglobal = 0
totalprocesos = 0
processmax = 3
lotes = 0

class proceso:
    def __init__(self,operacion,tiempomax,id,resultado):
        self.operacion = operacion
        self.tiempomax = tiempomax
        self.id = id
        self.resultado = resultado
        self.llegada = "NA"
        self.finalizacion = "NA"
        self.retorno = "NA"
        self.respuesta = "NA"
        self.espera = "NA"
        self.servicio = "NA"
        self.bandera = False
    
    def setResultado(self,op):
        self.resultado = op
        
        

def clearscreen():
    os.system('cls' if os.name=='nt' else 'clear')

def definirprocesos():
    global totalprocesos
    global idlist
    global splittedlist
    '''
    TOTAL DE PROCESOS
    '''
    while True:
        try:
            print("**********************************************")
            print("*    SIMULADOR DE PROCESAMIENTO POR LOTES    *")
            print("**********************************************")
            totalprocesos = int(input("Ingrese el total de procesos: "))
            if totalprocesos > 0:
                break
            else:
                print("El total de procesos debe ser mayor a 0")
                continue
        except:
            print("El numero de procesos debe ser un valor entero")
    print("Campo validado")
    
    '''
    PEDIR DATOS
    '''
    clearscreen()
    idauto = 0
    for i in range(totalprocesos): 
        idauto += 1
        idprocess = idauto
        #VALIDACION DE ID
        
        op = random.randint(1,6)
     
        if op == 1:
            v1 = random.randint(1,50)
            v2 = random.randint(1,50)
            resultado = v1 + v2
            operacion = str(v1) + "+" + str(v2)
                    
        elif op == 2:
            v1 = random.randint(1,50)
            v2 = random.randint(1,50)
            resultado = v1 - v2
            operacion = str(v1) + "-" + str(v2)
                    
        elif op == 3:
            v1 = random.randint(1,50)
            v2 = random.randint(1,50)        
            resultado = v1 / v2
            operacion = str(v1) + "/" + str(v2)
                           
                        
        elif op == 4:
            v1 = random.randint(1,50)
            v2 = random.randint(1,50)
            resultado = v1 * v2
            operacion = str(v1) + "*" + str(v2)
                    
        elif op == 5:
            v1 = random.randint(1,50)
            v2 = random.randint(1,50)          
            resultado = v1 % v2
            operacion = str(v1) + "%" + str(v2)
                            
        elif op == 6:
            v1 = random.randint(1,50)
            v2 = random.randint(1,50)
            resultado = math.pow(v1,v2)
            operacion = str(v1) + "^" + str(v2)
                    
        
        
        #VALIDAR TIEMPO MAXIMO
        tiempomax = random.randint(5,7)
       
        
        #GUARDAR OBJETO EN LA LISTA
        p1 = proceso(operacion,tiempomax,idprocess,resultado)
        masterlist.append(p1)

    clearscreen()
    procesamiento()
    
 
def procesamiento():
    longmaster = len(masterlist)
    finalizado = False
    globalcounter = 0
    nuevos = masterlist
    listos = []
    ejecucion = []
    bloqueados = []
    terminados = []
    #LLENAR LISTOS POR PRIMERA VEZ
    for i in range(3):
        if nuevos:
            nuevos[0].llegada = globalcounter
            listos.append(nuevos[0])
            del nuevos[0]
    
    if listos:
        if listos[0].bandera == False:
            listos[0].respuesta = globalcounter
            listos[0].bandera = True
            listos[0].servicio = 0
        ejecucion.append(listos[0])
        del listos[0]
    
    while finalizado == False:
        restantes = len(nuevos)
        print("Contador global: ",globalcounter)
        print("Procesos nuevos: ", restantes)
        print('\n')
        print("--------------------------------------------")
        print("PROCESOS LISTOS")
        print('\n')
        print("ID | TME |  TT")
        for proceso in listos:
            print(proceso.id," | ",proceso.tiempomax," | ",proceso.servicio)
        #Ejecucion
        print('\n')
        print("--------------------------------------------")
        print("PROCESO EN EJECUCION")
        print('\n')
        print("ID | TME |  TT")
        for proceso in ejecucion:
            print(proceso.id," | ",proceso.tiempomax," | ",proceso.servicio)
            proceso.servicio += 1
        
        #Terminados
        print('\n')
        print("--------------------------------------------")
        print("PROCESOS TERMINADOS")
        print('\n')
        print("ID | OP |  RES | TLL | TFIN | TSER | TRET | TRES | TME")
        for proceso in terminados:
            print(proceso.id," | ",proceso.operacion," | ",proceso.resultado," | ",proceso.llegada," | ",proceso.finalizacion," | ",proceso.servicio," | ",proceso.retorno," | ",proceso.respuesta," | ",proceso.tiempomax)
            
        
        globalcounter += 1 
        #Finalizacion normal
        if len(ejecucion) > 0:
            if ejecucion[0].servicio == ejecucion[0].tiempomax:
                ejecucion[0].finalizacion = globalcounter
                ejecucion[0].retorno = ejecucion[0].finalizacion - ejecucion[0].llegada
                ejecucion[0].espera = ejecucion[0].retorno - ejecucion[0].servicio
                terminados.append(ejecucion[0])
                del ejecucion[0]
                if len(nuevos) > 0:
                    nuevos[0].llegada = globalcounter
                    listos.append(nuevos[0])
                    del nuevos[0]

        #Entrada a ejecucion
        if len(ejecucion) == 0:
            if len(listos)>0:
                if listos[0].bandera == False:
                    listos[0].respuesta = globalcounter
                    listos[0].bandera = True
                    listos[0].servicio = 0
                ejecucion.append(listos[0])
                del listos[0]

        if(len(terminados) == longmaster):
            finalizado = True
        time.sleep(1)
        clearscreen()
    

    clearscreen()
    print("Contador global: ",globalcounter)
    print("Procesos nuevos: 0")
    print("--------------------------------------------")
    print("PROCESOS TERMINADOS")
    print('\n')
    print("ID | OP |  RES | TLL | TFIN | TSER | TRET | TRES | TME")
    for proceso in terminados:
        print(proceso.id," | ",proceso.operacion," | ",proceso.resultado," | ",proceso.llegada," | ",proceso.finalizacion," | ",proceso.servicio," | ",proceso.retorno," | ",proceso.respuesta," | ",proceso.tiempomax)

    input("PROCESO FINALIZADO")
        
        
 
    
def main():
    clearscreen()
    definirprocesos()
    

if __name__=='__main__':
    main()