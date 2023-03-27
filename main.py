# Pablo Hernandez Martinez, pablo.hernandez.martinez@udc.es - Marcelo Ferreiro Sánchez, marcelo.fsanchez@udc.es
import sys
import pandas as pd
from avion import Avion
from cola import Cola

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

        stats = pd.DataFrame({
            'Nombre': [],
            'Clase': [],
            'Tiempo de espera': []
        })
        
        time = 0
        while True:
            # modificar y mostrar el tiempo
            time += 1
            print('t:', time)
                        
            if cola_de_despegues.is_empty() is False: # coger el primer vuelo, registrar el tiempo de despegue y quitarlo de la cola de despegues
                primer_vuelo = cola_de_despegues.dequeue()
                primer_vuelo.set_entry_time(time)
                lista_de_colas_de_pista[primer_vuelo.get_priority() - 1].enqueue(primer_vuelo)
                
                print('Entrando en pista vuelo con ID: {IDVuelo}\tPrioridad: {Clase}\tt actual: {TActual}'.format(
                    IDVuelo = primer_vuelo.get_name(),
                    Clase = primer_vuelo.get_priority(),
                    TActual = time
                ))
                
                current_stats = pd.DataFrame({'Nombre': primer_vuelo.get_name(), 'Clase': primer_vuelo.get_flight_class(), 'Tiempo de espera': [0]})
                pd.concat([stats, current_stats])
                

            #comprobar si queda algún avión en alguna cola de despegue
            for i in lista_de_colas_de_pista:
                if i.is_empty() is False:
                    quedan_aviones = True
                    break
                else:
                    quedan_aviones = False

            if quedan_aviones: # si quedan aviones, hacer que despeguen y gestionar los retrasos
                # despegue
                if time % 5 == 0:
                    for i in lista_de_colas_de_pista:
                        if i.is_empty() is False:
                            despegue = i.dequeue()
                            despegue.set_wait_time(time - despegue.get_entry_time())
                            # indice del avion que despega = 
                            # df.loc[df['col1'] == value]
                            indice = stats.loc[stats['Nombre'] == despegue.get_name()]
                            stats.at[indice, 'Tiempo de espera']
                            
                            
                            print('Despegando vuelo con ID: {IDVuelo}\tPrioridad: {Clase}\tt de entrada en pista: {TEntrada_PISTA}\tt: {TActual}'.format(
                                IDVuelo = despegue.get_name(),
                                Clase = despegue.get_priority(),
                                TEntrada_PISTA = despegue.get_entry_time(),
                                TActual = time
                            ))
                            break
                
                # reprogramar los vuelos que tengan más de 20 unidades de retraso
                for i in lista_de_colas_de_pista:
                    if i.is_empty() is False:
                        avion = i.first()
                        if (time - avion.get_entry_time()) > 20 and avion.get_priority() > 1:
                            i.remove(avion)
                            avion.set_priority(avion.get_priority() - 1)
                            avion.set_entry_time(time)
                            print('Entrando en pista vuelo con ID: {IDVuelo}\tPrioridad: {Clase}\tt actual: {TActual}'.format(
                                IDVuelo = primer_vuelo.get_name(),
                                Clase = primer_vuelo.get_priority(),
                                TActual = time
                            ))
                            lista_de_colas_de_pista[avion.get_priority()].enqueue(avion)

            else: # si ya no quedan aviones en ninguna de las dos colas
                print(stats)
                
                '''
                wait_stats_series = [pd.Series(stats[fila], name = fila) for fila in stats] 
                
                print('\n---------------------------------------------')
                print('| Clase\t\t| Tiempo de espera promedio |')
                print('---------------------------------------------')
                for serie in wait_stats_series:
                    print('| {c}\t| {m}\t\t\t    |'.format(
                        c = serie.name,
                        m = round(serie.mean(), 2)
                    ))
                print('---------------------------------------------\n')
                '''
                break

if __name__ == "__main__":
    run(sys.argv[1])