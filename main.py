# Pablo Hernandez Martinez, pablo.hernandez.martinez@udc.es - Marcelo Ferreiro Sánchez, marcelo.fsanchez@udc.es
import sys
import warnings
import pandas as pd
from avion import Avion
from cola import Cola
warnings.simplefilter(action='ignore', category=FutureWarning)
# solo usamos la librería warnings para que al usuario no le
# salten las advertencias de que un método está obsoleto

def parse_params(params):
    '''
    '''
    nombre, clase = params[0], params[1].lower()
    
    if clase == 'domestico':
        prioridad = 1
    elif clase == 'privado':
        prioridad = 2
    elif clase == 'regular':
        prioridad = 3
    elif clase == 'charter':
        prioridad = 4
    elif clase == 'transoceanico':
        prioridad = 5
    
    return Avion(nombre, clase, prioridad)

def run(path):
    '''
    '''
    with open(path) as f:
        cola_de_despegues, lista_de_colas_de_pista = Cola(), [Cola(), Cola(), Cola(), Cola(), Cola()]

        for elemento in f.readlines():
            cola_de_despegues.enqueue(parse_params(elemento.split()))

        stats = {
            'Nombre': [],
            'Clase': [],
            'Tiempo de espera': []
        }
        
        time = 0
        while True:
            # modificar y mostrar el tiempo
            time += 1
            print('Tiempo actual:', time)
            
            if cola_de_despegues.is_empty() is False: # coger el primer vuelo, registrar el tiempo de despegue y quitarlo de la cola de despegues
                primer_vuelo = cola_de_despegues.dequeue()
                primer_vuelo.set_entry_time(time)
                lista_de_colas_de_pista[primer_vuelo.get_priority() - 1].enqueue(primer_vuelo)
                
                print('Entrando en pista vuelo con ID: {IDVuelo}\tPrioridad: {Clase}\tt actual: {TActual}'.format(
                    IDVuelo = primer_vuelo.get_name(),
                    Clase = primer_vuelo.get_priority(),
                    TActual = time
                ))
                                                
            #comprobar si queda algún avión en alguna cola de despegue
            for i in lista_de_colas_de_pista:
                if i.is_empty():
                    quedan_aviones = False
                else:
                    quedan_aviones = True
                    break

            if quedan_aviones: # si quedan aviones, hacer que despeguen y gestionar los retrasos
                # despegue
                if time % 5 == 0:
                    for i in lista_de_colas_de_pista:
                        if i.is_empty() is False:
                            despegue = i.dequeue()                
                            print('Despegando vuelo con ID: {IDVuelo}\tPrioridad: {Clase}\tt de entrada en pista: {TEntrada_PISTA}\tt: {TActual}'.format(
                                IDVuelo = despegue.get_name(),
                                Clase = despegue.get_priority(),
                                TEntrada_PISTA = despegue.get_entry_time(),
                                TActual = time
                            ))
                            
                            # modificar las estadísticas
                            stats['Nombre'].append(despegue.get_name())
                            stats['Clase'].append(despegue.get_flight_class())
                            stats['Tiempo de espera'].append(time - despegue.get_entry_time())                            

                            break
                
                # reprogramar los vuelos que tengan más de 20 unidades de retraso
                for i in lista_de_colas_de_pista:
                    if i.is_empty() is False:
                        avion = i.first()
                        if (time - avion.get_entry_time()) > 20 and avion.get_priority() > 1:
                            i.dequeue()
                            avion.set_priority(avion.get_priority() - 1)
                            avion.set_entry_time(time)
                            lista_de_colas_de_pista[avion.get_priority() - 1].enqueue(avion)
                            
                            print('Entrando en pista vuelo con ID: {IDVuelo}\tPrioridad: {Clase}\tt actual: {TActual}'.format(
                                IDVuelo = avion.get_name(),
                                Clase = avion.get_priority(),
                                TActual = time
                            ))
                                        
            else: # si ya no quedan aviones en ninguna de las dos colas
                stats = pd.DataFrame(stats)
                print('\n',
                      stats.groupby('Clase').mean(),
                      '\n')
                break

if __name__ == "__main__":
    run(sys.argv[1])