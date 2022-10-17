from doctest import master
from glob import glob
import os
import math
import time
import random
from typing import final
import keyboard


masterlist = []
nuevos = []
splittedlist = []
idlist = []
contadorglobal = 0
totalprocesos = 0
processmax = 3
lotes = 0
idauto = 0

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
        self.tbloqueado = "NA"
        self.restante = self.tiempomax
        self.emomento = self.espera
    
    def setResultado(self,op):
        self.resultado = op
    
    def setRestante(self):
        if self.servicio != "NA":
            self.restante = self.tiempomax - self.servicio
    def setEMomento(self,contador):
        if self.llegada != "NA" and self.servicio != "NA":
            self.emomento = contador - self.llegada - self.servicio
        
        
        

def clearscreen():
    os.system('cls' if os.name=='nt' else 'clear')

def definirprocesos():
    global totalprocesos
    global idlist
    global splittedlist
    global idauto
    '''
    TOTAL DE PROCESOS
    '''
    while True:
        try:
            print("**********************************************")
            print("*           FIRST COME FIRST SERVED          *")
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
        tiempomax = random.randint(6,16)
       
        
        #GUARDAR OBJETO EN LA LISTA
        p1 = proceso(operacion,tiempomax,idprocess,resultado)
        masterlist.append(p1)

    clearscreen()
    procesamiento()

def agregarp():
    global idauto
    global nuevos
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
    tiempomax = random.randint(6,16)
       
        
    #GUARDAR OBJETO EN LA LISTA
    p1 = proceso(operacion,tiempomax,idprocess,resultado)
    nuevos.append(p1)

    
 
def procesamiento():
    global nuevos
    memoria = 0
    pausado = False
    error = False
    interrupcion = False
    longmaster = len(masterlist)
    finalizado = False
    Nulo = False
    BCP = False
    globalcounter = 0
    nuevos = masterlist
    listos = []
    ejecucion = []
    bloqueados = []
    terminados = []

    #LLENAR LISTOS POR PRIMERA VEZ
    for i in range(3):
        if nuevos:
            memoria += 1
            nuevos[0].llegada = globalcounter
            listos.append(nuevos[0])
            del nuevos[0]
    #Mandar primer proceso a ejecución
    if listos:
        if listos[0].bandera == False:
            listos[0].respuesta = globalcounter - listos[0].llegada
            listos[0].bandera = True
            listos[0].servicio = 0
        ejecucion.append(listos[0])
        del listos[0]
    
    while finalizado == False:
        memoria = len(listos) + len(ejecucion) + len(bloqueados)
        while memoria < 3 and len(nuevos) >= 1:
            nuevos[0].llegada = globalcounter
            listos.append(nuevos[0])
            del nuevos[0]
            memoria += 1
        if pausado == False and BCP == False:
            restantes = len(nuevos)
            print("MEMORIA: ",memoria)
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
            if Nulo == True:
                print("NULL | NULL | NULL ")
            for proceso in ejecucion:
                print(proceso.id," | ",proceso.tiempomax," | ",proceso.servicio)
                proceso.servicio += 1
            #Bloqueados
            print('\n')
            print("--------------------------------------------")
            print("PROCESOS BLOQUEADOS")
            print('\n')
            print("ID | TT en B")
            for proceso in bloqueados:
                print(proceso.id," | ",proceso.tbloqueado)
                proceso.tbloqueado += 1
            
        
            #Terminados
            print('\n')
            print("--------------------------------------------")
            print("PROCESOS TERMINADOS")
            print('\n')
            print("ID | OP |  RES | TLL | TFIN | TSER | TRET | TRES | ESP | TME")
            for proceso in terminados:
                print(proceso.id," | ",proceso.operacion," | ",proceso.resultado," | ",proceso.llegada," | ",proceso.finalizacion," | ",proceso.servicio," | ",proceso.retorno," | ",proceso.respuesta," | ",proceso.espera," | ",proceso.tiempomax)
            
            globalcounter += 1 

        #PAUSADO
        if pausado == True and BCP == False:
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
            if Nulo == True:
                print("NULL | NULL | NULL ")
            for proceso in ejecucion:
                print(proceso.id," | ",proceso.tiempomax," | ",proceso.servicio)
            #Bloqueados
            print('\n')
            print("--------------------------------------------")
            print("PROCESOS BLOQUEADOS")
            print('\n')
            print("ID | TT en B")
            for proceso in bloqueados:
                print(proceso.id," | ",proceso.tbloqueado)
            
        
            #Terminados
            print('\n')
            print("--------------------------------------------")
            print("PROCESOS TERMINADOS")
            print('\n')
            print("ID | OP |  RES | TLL | TFIN | TSER | TRET | TRES | ESP | TME")
            for proceso in terminados:
                print(proceso.id," | ",proceso.operacion," | ",proceso.resultado," | ",proceso.llegada," | ",proceso.finalizacion," | ",proceso.servicio," | ",proceso.retorno," | ",proceso.respuesta," | ",proceso.espera," | ",proceso.tiempomax)


        #DESPLEGAR BCP
        if BCP == True:
            clearscreen()
            print("TABLA DE PROCESOS")
            print("CONTADOR GLOBAL: ",globalcounter)
            print("ID | ESTADO | OPERACION | RESULTADO | TLL | TF | TR | TE | TS | TRES | TRESP")
            for i in nuevos:
                print(i.id," | ","NUEVOS"," | ",i.operacion," | ","NA"," | ",i.llegada," | ",i.finalizacion," | ",i.retorno," | ",i.espera," | ",i.servicio," | ","NA"," | ",i.respuesta)
            for i in listos:
                i.setEMomento(globalcounter)
                i.setRestante()
                print(i.id," | ","LISTOS"," | ",i.operacion," | ","NA"," | ",i.llegada," | ",i.finalizacion," | ",i.retorno," | ",i.emomento," | ",i.servicio," | ",i.restante," | ",i.respuesta)
            for i in ejecucion:
                i.setEMomento(globalcounter)
                i.setRestante()
                print(i.id," | ","EJECUCION"," | ",i.operacion," | ","NA"," | ",i.llegada," | ",i.finalizacion," | ",i.retorno," | ",i.emomento," | ",i.servicio," | ",i.restante," | ",i.respuesta)
            for i in terminados:
                print(i.id," | ","FINALIZADOS"," | ",i.operacion," | ",i.resultado," | ",i.llegada," | ",i.finalizacion," | ",i.retorno," | ",i.espera," | ",i.servicio," | ","NA"," | ",i.respuesta)

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
                    listos[0].respuesta = globalcounter - listos[0].llegada
                    listos[0].bandera = True
                    listos[0].servicio = 0
                ejecucion.append(listos[0])
                del listos[0]
                Nulo = False
            else:
                Nulo = True
        #Fin proceso
        if(len(terminados) == longmaster):
            finalizado = True
        
        #Salida de bloqueados
        if(len(bloqueados) > 0):
            if bloqueados[0].tbloqueado == 7:
                bloqueados[0].tbloqueado = 0
                listos.append(bloqueados[0])
                del bloqueados[0]

        #Finalizacion por error
        if error == True:
            if len(ejecucion) > 0:
                ejecucion[0].finalizacion = globalcounter
                ejecucion[0].retorno = ejecucion[0].finalizacion - ejecucion[0].llegada
                ejecucion[0].espera = ejecucion[0].retorno - ejecucion[0].servicio
                ejecucion[0].resultado = "ERROR"
                terminados.append(ejecucion[0])
                del ejecucion[0]
                if len(nuevos) > 0:
                    nuevos[0].llegada = globalcounter
                    listos.append(nuevos[0])
                    del nuevos[0]
            error = False

        #Envio a bloqueados
        if interrupcion == True:
            if len(ejecucion)>0:
                ejecucion[0].tbloqueado = 0
                bloqueados.append(ejecucion[0])
                del ejecucion[0]
            interrupcion = False

        if keyboard.is_pressed('w') and pausado == False:
            error = True
        if keyboard.is_pressed('e') and pausado == False:
            interrupcion = True
        if keyboard.is_pressed('p'):
            pausado = True
        if keyboard.is_pressed('c'):
            pausado = False
            BCP = False
        if keyboard.is_pressed('n'):
            agregarp()
            longmaster += 1
        if keyboard.is_pressed('b'):
            BCP = True

        time.sleep(1)
        clearscreen()

    clearscreen()
    print("Contador global: ",globalcounter)
    print("Procesos nuevos: 0")
    print("--------------------------------------------")
    print("PROCESOS TERMINADOS")
    print('\n')
    print("ID | OP |  RES | TLL | TFIN | TSER | TRET | TRES | ESP | TME")
    for proceso in terminados:
        print(proceso.id," | ",proceso.operacion," | ",proceso.resultado," | ",proceso.llegada," | ",proceso.finalizacion," | ",proceso.servicio," | ",proceso.retorno," | ",proceso.respuesta," | ",proceso.espera," | ",proceso.tiempomax)

    input("PROCESO FINALIZADO")
        
        
 
    
def main():
    clearscreen()
    definirprocesos()
    

if __name__=='__main__':
    main()