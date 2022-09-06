import os
import math
import time
import random
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
        self.estado = 0

    def setEstado(self,estado):
        self.estado = estado
    
    def getEstado(self):
        return self.estado
    
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
        tiempomax = random.randint(1,7)
       
        
        #GUARDAR OBJETO EN LA LISTA
        p1 = proceso(operacion,tiempomax,idprocess,resultado)
        masterlist.append(p1)

    splitlist()
    clearscreen()
    procesamiento()
    
 
def procesamiento():
    pausado = False
    error = False
    interrupcion = False
    counterlotes = []
    tiempores = 0
    countlot = 1
    listfinal = []
    global contadorglobal
    global lotes
    terminado = False
    auxlist = []
    i = 0
    tiempotrans = 0
    tiempomx = 0
    j = splittedlist[0]
    del splittedlist[0]
    while True:
        if terminado == True:
            lotes = lotes - 1
            if(splittedlist):
                j = splittedlist[0]
                del splittedlist[0]
                countlot += 1
                terminado = False
            else:
                lotes = 0
                print("-----------------------------------------------")
                print("Contador Global: ",contadorglobal)
                print("Lotes restantes: ",lotes)
                print("-------------------------------------------------------------")
                print("Lote en ejecucion: ")
                print("PROGRAMADOR  |  TIEMPO MAXIMO ESPERADO")
                print("-------------------------------------------------------------")
                print("Proceso en ejecucion: ")
                print("NOMBRE|OPERACION|TIEMPO MAXIMO ESPERADO| NUMERO DE PROGRAMA")
                print("-----------------------------------------------")
                print("-------------------------------------------------------------")
                print("Procesos Terminados: ")
                print("NUMERO DE PROGRAMA|OPERACION|RESULTADO| LOTE")
                loti = 0
                for term in listfinal:
                    print(term.id,"   |   ",term.operacion,"    |    ",term.resultado,"    |        ",counterlotes[loti])
                    loti += 1
                input("Proceso terminado, presiona ENTER para finalizar")
                break
        
        if i == totalprocesos:
            break
        if pausado == False:
            contadorglobal +=1
        
        if(tiempotrans == tiempomx):
            auxlist = []
            if j:
                auxlist.append(j[0])
                tiempomx = auxlist[0].tiempomax
                tiempotrans = auxlist[0].estado
                tiempores = tiempomx-tiempotrans
                del j[0]
                
            else:
                terminado = True
        if pausado == True:
            print("-------------------------------------------------------------")
            print("Contador Global: ",contadorglobal)
            print("Lotes restantes: ",lotes)
            print("-------------------------------------------------------------")
            print("Lote en ejecucion: ")
            print("PROGRAMADOR  |  TIEMPO MAXIMO ESPERADO")
            for proc in j:
                print(proc.id,"         ",proc.tiempomax)
            print("-------------------------------------------------------------")
            print("Proceso en ejecucion: ")
            print("ID|OPERACION|TIEMPO MAXIMO ESPERADO| NUMERO DE PROGRAMA")
            print(auxlist[0].id,"    |    ",auxlist[0].operacion,"    |    ",auxlist[0].tiempomax,"    |    ",auxlist[0].id)
            print("TIEMPO TRANSCURRIDO: ",tiempotrans)
            print("TIEMPO RESTANTE POR EJECUTAR:",tiempores)
            
            print("-------------------------------------------------------------")
            print("Procesos Terminados: ")
            print("NUMERO DE PROGRAMA|OPERACION|RESULTADO| LOTE")
            loti = 0
            for term in listfinal:
                print(term.id,"   |   ",term.operacion,"    |    ",term.resultado,"    |        ",counterlotes[loti])
                loti += 1

        if(terminado != True and pausado == False):
            print("-------------------------------------------------------------")
            print("Contador Global: ",contadorglobal)
            print("Lotes restantes: ",lotes)
            print("-------------------------------------------------------------")
            print("Lote en ejecucion: ")
            print("PROGRAMADOR  |  TIEMPO MAXIMO ESPERADO")
            for proc in j:
                print(proc.id,"         ",proc.tiempomax)
            print("-------------------------------------------------------------")
            print("Proceso en ejecucion: ")
            print("ID|OPERACION|TIEMPO MAXIMO ESPERADO| NUMERO DE PROGRAMA")
            print(auxlist[0].id,"    |    ",auxlist[0].operacion,"    |    ",auxlist[0].tiempomax,"    |    ",auxlist[0].id)
            print("TIEMPO TRANSCURRIDO: ",tiempotrans)
            print("TIEMPO RESTANTE POR EJECUTAR:",tiempores)
            
            print("-------------------------------------------------------------")
            print("Procesos Terminados: ")
            print("NUMERO DE PROGRAMA|OPERACION|RESULTADO| LOTE")
            loti = 0
            for term in listfinal:
                print(term.id,"   |   ",term.operacion,"    |    ",term.resultado,"    |        ",counterlotes[loti])
                loti += 1
            if not j and tiempotrans == tiempomx:
                terminado = True
            tiempotrans += 1
            tiempores = tiempores - 1
            if tiempotrans == tiempomx and error != True:
                listfinal.append(auxlist[0])
                counterlotes.append(countlot)
        

        if keyboard.is_pressed('w') and pausado == False:
            error = True
        if keyboard.is_pressed('e') and pausado == False:
            interrupcion = True
        if keyboard.is_pressed('p'):
            pausado = True
        if keyboard.is_pressed('c'):
            pausado = False
        
        if error == True:
            auxlist[0].setResultado("Error")
            listfinal.append(auxlist[0])
            counterlotes.append(countlot)
            auxlist = []
            if j:
                auxlist.append(j[0])
                tiempomx = auxlist[0].tiempomax
                tiempotrans = auxlist[0].estado
                tiempores = tiempomx-tiempotrans
                del j[0]
                
                error = False

            else:
                terminado = True
                error = False
        
        if interrupcion == True:
            auxlist[0].setEstado(tiempotrans)
            j.append(auxlist[0])
            auxlist = []
            if j:
                auxlist.append(j[0])
                tiempomx = auxlist[0].tiempomax
                tiempotrans = auxlist[0].estado
                tiempores = tiempomx-tiempotrans
                del j[0]
                interrupcion = False
        

        time.sleep(1)
        clearscreen()
        
        
 
    
def splitlist():
    global lotes
    listaux = []
    j = 0
    counter = 0
    for i in masterlist:
        if j < 2:
            listaux.append(i)
            j = j + 1
        else:
            listaux.append(i)
            splittedlist.append(listaux)
            lotes += 1
            listaux = []
            j = 0
    splittedlist.append(listaux)
    
    
def main():
    clearscreen()
    definirprocesos()
    

if __name__=='__main__':
    main()