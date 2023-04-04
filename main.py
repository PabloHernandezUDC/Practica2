# Pablo Hernandez Martinez, pablo.hernandez.martinez@udc.es - Marcelo Ferreiro Sánchez, marcelo.fsanchez@udc.es
import sys, warnings
import pandas as pd
import matplotlib.pyplot as plt
from avion import Avion
from cola import Cola
warnings.simplefilter(action='ignore', category=FutureWarning) # just to avoid printing deprecation warnings

def parse_params(params):
    '''
    This function reads the data from the text file containing the information about the flights and hands out that data in a format
    that is functional for the following function.
    ---------- 
    params: str 
        Text line with a certain format that will be used for Avion object creation.
 
    Returns 
    ------- 
    Avion
        Avion object with several parameters that were fetched from the file that was read
    '''
    nombre, clase = params[0], params[1].lower()
    lista_de_clases = ['domestico', 'privado', 'regular', 'charter', 'transoceanico']
    
    for i in lista_de_clases:
        if i == clase:
            prioridad = lista_de_clases.index(i) + 1
            break
        
    return Avion(nombre, clase, prioridad)

def run(path):
    '''
    This function runs one iteration of the simulation based on a given text file with a certain format.
    If the file meets the format criteria, it will be read correctly and characters will be created from the parse_params function.
    Parameters 
    ---------- 
    path: str 
        File path for the file that will be used. 
 
    Returns 
    ------- 
    stats:
        All of the information that the exercise requires from the program, Name, Class and Waiting time.
    '''
    with open(path) as f:
        cola_de_despegues, lista_de_colas_de_pista = Cola(), [Cola(), Cola(), Cola(), Cola(), Cola()]
        # Here the funcion gets access to the flight data via the parse_params function.
        for elemento in f.readlines():
            cola_de_despegues.enqueue(parse_params(elemento.split()))

        #creates an empty dictionary with the required stats.
        stats = {
            'Nombre': [],
            'Clase': [],
            'Tiempo de espera': []
        }
        #creates the time loop.
        time = 0
        while True:
            time += 1
            print('Tiempo actual:', time)
            #This loop enqueues a plane from the flight departures list into the track when the departure queue is not empty.
            if cola_de_despegues.is_empty() is False:
                primer_avion = cola_de_despegues.dequeue()
                primer_avion.set_original_entry_time(time)
                lista_de_colas_de_pista[primer_avion.get_priority() - 1].enqueue(primer_avion)
                
                print('Entrando en pista vuelo con ID: {id_vuelo}\tPrioridad: {clase}\tt actual: {t_actual}'.format(
                    id_vuelo = primer_avion.get_name(),
                    clase = primer_avion.get_priority(),
                    t_actual = time
                ))
                                                
            for i in lista_de_colas_de_pista:
                if i.is_empty():
                    quedan_aviones = False
                else:
                    quedan_aviones = True
                    break

            if quedan_aviones:
                if time % 5 == 0:
                    for i in lista_de_colas_de_pista:
                        if i.is_empty() is False:
                            despegue = i.dequeue()                
                            print('Despegando vuelo con ID: {id_vuelo}\tPrioridad: {clase}\tt de entrada en pista: {t_entrada_pista} t actual: {t_actual}'.format(
                                id_vuelo = despegue.get_name(),
                                clase = despegue.get_priority(),
                                t_entrada_pista = despegue.get_original_entry_time(),
                                t_actual = time
                            ))
                            
                            stats['Nombre'].append(despegue.get_name())
                            stats['Clase'].append(despegue.get_flight_class())
                            stats['Tiempo de espera'].append(time - despegue.get_original_entry_time())                            
                            break
                
                for i in lista_de_colas_de_pista:
                    if i.is_empty() is False:
                        avion = i.first()
                        if avion.get_new_entry_time() == 0:
                            avion.set_wait_time(time - avion.get_original_entry_time())
                        else:
                            avion.set_wait_time(time - avion.get_new_entry_time())
                            
                        if time - avion.get_wait_time() > 20 and avion.get_priority() > 1:
                            i.dequeue()
                            avion.set_priority(avion.get_priority() - 1)
                            avion.set_new_entry_time(time)
                            lista_de_colas_de_pista[avion.get_priority() - 1].enqueue(avion)
                            
                            print('Reubicando vuelo con ID: {id_vuelo}\tPrioridad: {clase}\tt actual: {t_actual}'.format(
                                id_vuelo = avion.get_name(),
                                clase = avion.get_priority(),
                                t_actual = time
                            ))

            else:
                stats = pd.DataFrame(stats)
                break

    return stats

if __name__ == "__main__":
    result = run(sys.argv[1])
    print('\n', result.groupby('Clase').mean(), '\n')
    result.plot.scatter(x = "Clase", y = "Tiempo de espera", c = 'Tiempo de espera', colormap = 'viridis')
    plt.show()