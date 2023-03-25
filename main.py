# Pablo Hernandez Martinez, pablo.hernandez.martinez@udc.es - Marcelo Ferreiro Sánchez, marcelo.fsanchez@udc.es
import sys
import pandas as pd
from avion import Avion
from cola import Cola

def parse_params(params):
    '''
    '''
    nombre, prioridad = params[0], params[1].lower()
    
    if prioridad == 'domestico':
        prioridad = 1
    elif prioridad == 'privado':
        prioridad = 2
    elif prioridad == 'regular':
        prioridad = 3
    elif prioridad == 'charter':
        prioridad = 4
    elif prioridad == 'transoceanico':
        prioridad = 5
    
    return Avion(nombre, prioridad)

def run(path):
    '''
    '''
    with open(path) as f:
        cola_de_despegues = Cola()
        for elemento in f.readlines():
            cola_de_despegues.enqueue(parse_params(elemento.split()))
        
        lista_de_colas_de_pista = [
            Cola(),
            Cola(),
            Cola(),
            Cola(),
            Cola(),
        ]

        wait_stats = {
                1: [],
                2: [],
                3: [],
                4: [],
                5: [],
            }
        
        time = 0
        while True:
            # modificar y mostrar el tiempo
            time += 1
            print('t:', time)
                        
            if cola_de_despegues.is_empty() == False:
                # coger el primer vuelo, registrar el tiempo de despegue y quitarlo de la cola de despegues
                primer_despegue = cola_de_despegues.dequeue()
                primer_despegue.set_entry_time(time)
                lista_de_colas_de_pista[primer_despegue.get_priority() - 1].enqueue(primer_despegue)
                print('Entrando en pista vuelo con ID: {IDVuelo}\tPrioridad: {Clase}\tt actual: {TActual}'.format(
                    IDVuelo = primer_despegue.get_name(),
                    Clase = primer_despegue.get_priority(),
                    TActual = time
                ))

            #comprobar si queda algún avión en alguna cola de despegue
            for i in lista_de_colas_de_pista:
                if i.is_empty() == False:
                    quedan_aviones = True
                    break
                else:
                    quedan_aviones = False

            if quedan_aviones:
                # despegue del que corresponda
                if time % 5 == 0:
                    for i in lista_de_colas_de_pista:
                        if i.is_empty() == False:
                            despegue = i.dequeue()
                            wait_stats[despegue.get_priority()].append(time - despegue.get_entry_time())
                            print('Despegando vuelo con ID: {IDVuelo}\tPrioridad: {Clase}\tt de entrada en pista: {TEntrada_PISTA}\tt es {TActual}'.format(
                                IDVuelo = despegue.get_name(),
                                Clase = despegue.get_priority(),
                                TEntrada_PISTA = despegue.get_entry_time(),
                                TActual = time
                            ))
                            break
                        else:
                            pass
                
                # reprogramar los vuelos que tengan más de 20 unidades de retraso
                for i in lista_de_colas_de_pista:
                    if i.is_empty() == False:
                        for avion in i.data:
                            if (time - avion.get_entry_time()) > 20 and avion.get_priority() > 1:
                                avion = i.dequeue()
                                avion.set_priority(avion.get_priority() - 1)
                                avion.set_entry_time(time)
                                lista_de_colas_de_pista[avion.get_priority()].enqueue(avion)

            else:
                break
            
        return None

if __name__ == "__main__":
    run(sys.argv[1])