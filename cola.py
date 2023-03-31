# Pablo Hernandez Martinez, pablo.hernandez.martinez@udc.es - Marcelo Ferreiro Sánchez, marcelo.fsanchez@udc.es
class Cola():
    '''
    '''
    
    def __init__(self):
        '''
        '''
        self.data = []
        self.size = 0
    
    def update_size(self):
        self.size = len(self.data)
    
    def enqueue(self, e):
        '''
        '''
        self.data += [e]
        self.update_size()
        
    def dequeue(self):
        '''
        '''
        if self.is_empty() is False:
            e = self.first()
            self.data = self.data[1:]
            self.update_size()
            return e
        else:
            return None
    
    def first(self):
        '''
        '''
        return self.data[0]

    def is_empty(self):
        '''
        '''
        return self.size == 0