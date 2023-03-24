# Pablo Hernandez Martinez, pablo.hernandez.martinez@udc.es - Marcelo Ferreiro Sánchez, marcelo.fsanchez@udc.es
import sys, pandas
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

def run(path, time = 0):
    '''
    '''
    with open(path) as f:
        lines = f.readlines()
        cola_de_despegues = Cola()
        for elemento in lines:
            cola_de_despegues.enqueue(parse_params(elemento.split()))
        
        lista_de_colas_de_pista = [
            Cola(),
            Cola(),
            Cola(),
            Cola(),
            Cola(),
        ]

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
                            print('Despegando vuelo con ID: {IDVuelo}\tPrioridad: {Clase}\tt de entrada en pista: {TEntrada_PISTA}\tt es {TActual}'.format(
                                IDVuelo = despegue.get_name(),
                                Clase = despegue.get_priority(),
                                TEntrada_PISTA = despegue.get_entry_time(),
                                TActual = time
                            ))
                            break
                        else:
                            pass
                    
                for i in lista_de_colas_de_pista:
                    if i.is_empty() == False:
                        for avion in i.data:
                            if (avion.get_entry_time() - time) > 20 and avion.get_priority() > 1:
                                avion = i.dequeue()
                                avion.set_priority(avion.get_priority + 1)
                                avion.set_entry_time(time)
                                lista_de_colas_de_pista[avion.get_priority()].enqueue(avion)

            else:
                break
            
        return None

if __name__ == "__main__":
    run(sys.argv[1])