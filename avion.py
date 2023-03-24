class Avion():
    '''
    '''
    
    def __init__(self, name, priority, entry_time = 0):
        '''
        '''
        self.name = name
        self.priority = priority
    
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
