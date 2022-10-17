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
