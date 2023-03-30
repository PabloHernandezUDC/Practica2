# Pablo Hernandez Martinez, pablo.hernandez.martinez@udc.es - Marcelo Ferreiro Sánchez, marcelo.fsanchez@udc.es
class Avion():
    '''
    '''
    def __init__(self, name, flight_class, priority, entry_time = 0):
        '''
        '''
        self.name = name
        self.flight_class = flight_class
        self.priority = priority
            
    def get_name(self):
        '''
        '''
        return self.name
    
    def set_name(self, input_name):
        '''
        '''
        self.name = input_name
        
    def get_flight_class(self):
        '''
        '''
        return self.flight_class
    
    def set_flight_class(self, input_flight_class):
        '''
        '''
        self.flight_class = input_flight_class
        
    def get_priority(self):
        '''
        '''
        return self.priority
    
    def set_priority(self, input_priority):
        '''
        '''
        self.priority = input_priority

    def get_entry_time(self):
        '''
        '''
        return self.entry_time
    
    def set_entry_time(self, input_entry_time):
        '''
        '''
        self.entry_time = input_entry_time