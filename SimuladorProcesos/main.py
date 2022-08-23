import os
import math


masterlist = []
splittedlist = []
idlist = []
contadorglobal = 0
totalprocesos = 0
processmax = 3

class proceso:
    def __init__(self,programador,operacion,tiempomax,id,resultado):
        self.programador = programador
        self.operacion = operacion
        self.tiempomax = tiempomax
        self.id = id
        self.resultado = resultado
        

def clearscreen():
    os.system('cls' if os.name=='nt' else 'clear')

def definirprocesos():
    global totalprocesos
    global idlist
    '''
    TOTAL DE PROCESOS
    '''
    while True:
        try:
            totalprocesos = int(input("Bienvenido, ingrese el total de procesos"))
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
    
    for i in range(totalprocesos): 
        clearscreen()
        print("INGRESE LOS DATOS DEL PROCESO")
        programador = str(input("Ingrese el nombre del programador: "))
        #VALIDACION DE ID
        while True:
            try:
                idprocess = int(input("Ingrese la id del proceso: "))
                if idprocess in idlist:
                    print("Id ya repetida")
                else:
                    idlist.append(idprocess)
                    break
            except:
                print("El valor debe ser de tipo entero")     
        #VALIDACION DE OPERACION 
        while True:      
            print("Seleccione la operacion")
            print("1. SUMA")
            print("2. RESTA")
            print("3. DIVISION")
            print("4. MULTIPLICACION")
            print("5. RESIDUO")
            print("6. POTENCIA")
            try:
                op = int(input("Ingrese su operacion: "))
                if op == 1:
                    v1 = int(input("Ingrese el primer numero: "))
                    v2 = int(input("Ingrese el segundo numero: "))
                    resultado = v1 + v2
                    operacion = str(v1) + "+" + str(v2)
                    break
                elif op == 2:
                    v1 = int(input("Ingrese el primer numero: "))
                    v2 = int(input("Ingrese el segundo numero: "))
                    resultado = v1 - v2
                    operacion = str(v1) + "-" + str(v2)
                    break
                elif op == 3:
                    v1 = int(input("Ingrese el primer numero: "))
                    while True:
                        v2 = int(input("Ingrese el segundo numero: "))
                        if v2 != 0: 
                            resultado = v1 / v2
                            operacion = str(v1) + "/" + str(v2)
                            break
                        else:
                            print("El numero no puede ser 0")
                    break
                elif op == 4:
                    v1 = int(input("Ingrese el primer numero: "))
                    v2 = int(input("Ingrese el segundo numero: "))
                    resultado = v1 * v2
                    operacion = str(v1) + "*" + str(v2)
                    break 
                elif op == 5:
                    v1 = int(input("Ingrese el primer numero: "))
                    while True:
                        v2 = int(input("Ingrese el segundo numero: "))
                        if v2 != 0: 
                            resultado = v1 % v2
                            operacion = str(v1) + "%" + str(v2)
                            break
                        else:
                            print("El numero no puede ser 0")  
                    break 
                elif op == 6:
                    v1 = int(input("Ingrese el primer numero: "))
                    v2 = int(input("Ingrese el segundo numero: "))
                    resultado = math.pow(v1,v2)
                    operacion = str(v1) + "^" + str(v2)
                    break
                else:
                    print("No valido")
            except:
                print("Valor no valido")
        
        #VALIDAR TIEMPO MAXIMO
        while True:
            try:
                tiempomax = int(input("Ingrese el tiempo maximo: "))
                if tiempomax > 0:
                    print("Tiempo validado")
                    break
                else:
                    print("El tiempo debe ser mayor a 0")
            except: 
                print("El tipo de dato debe ser entero")
        
        #GUARDAR OBJETO EN LA LISTA
        p1 = proceso(programador,operacion,tiempomax,idprocess,resultado)
        masterlist.append(p1)
        print("Proceso Guardado")
        input("Presione ENTER para continuar.")

    splitlist()
    
    
def splitlist():
    print("Entra")
    listaux = []
    j = 0
    counter = 0
    for i in masterlist:
        if j < 3:
            listaux.append(i)
            j = j + 1
        else:
            splittedlist.append(listaux)
            listaux = []
            j = 0
    splittedlist.append(listaux)
    for j in splittedlist:
        counter += 1
        print("Lote: ",counter)
        for i in j:
            print(i.programador)
    
def main():
    print("Este es el main")
    p1 = proceso("Erick","1+2",23,34,33)
    masterlist.append(p1)
    for i in masterlist:
        print(i.programador)
    

if __name__=='__main__':
    definirprocesos()