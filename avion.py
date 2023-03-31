# Pablo Hernandez Martinez, pablo.hernandez.martinez@udc.es - Marcelo Ferreiro Sánchez, marcelo.fsanchez@udc.es
class Avion():
    '''
    '''
    def __init__(self, name, flight_class, priority):
        '''
        '''
        self.name = name
        self.flight_class = flight_class
        self.priority = priority
        self.original_entry_time = 0
        self.new_entry_time = 0
        self.wait_time = 0
            
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

    def get_original_entry_time(self):
        '''
        '''
        return self.original_entry_time
    
    def set_original_entry_time(self, input_original_entry_time):
        '''
        '''
        self.original_entry_time = input_original_entry_time
        
    def get_new_entry_time(self):
        '''
        '''
        return self.new_entry_time
    
    def set_new_entry_time(self, input_new_entry_time):
        '''
        '''
        self.new_entry_time = input_new_entry_time
        
    def get_wait_time(self):
        '''
        '''
        return self.wait_time
    
    def set_wait_time(self, input_wait_time):
        '''
        '''
        self.wait_time = input_wait_time