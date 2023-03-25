class Avion():
    '''
    '''
    
    def __init__(self, name, flight_class, priority, entry_time = 0, wait_time = 0):
        '''
        '''
        self.name = name
        self.flight_class = flight_class
        self.priority = priority
    
    def get_flight_class(self):
        '''
        '''
        return self.flight_class
    
    def set_flight_class(self, input_flight_class):
        '''
        '''
        self.flight_class = input_flight_class
        
    def get_name(self):
        '''
        '''
        return self.name
    
    def set_name(self, input_name):
        '''
        '''
        self.name = input_name
        
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

    def get_wait_time(self):
        '''
        '''
        return self.wait_time
    
    def set_wait_time(self, input_wait_time):
        '''
        '''
        self.wait_time = input_wait_time