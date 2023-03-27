# Pablo Hernandez Martinez, pablo.hernandez.martinez@udc.es - Marcelo Ferreiro Sánchez, marcelo.fsanchez@udc.es
class Cola():
    '''
    '''
    
    def __init__(self):
        '''
        '''
        self.data = []
        self.size = 0
    
    def enqueue(self, e):
        '''
        '''
        self.data += [e]
        self.size += 1
        
    def dequeue(self):
        '''
        '''
        if self.is_empty() is False:
            e = self.first()
            self.data = self.data[1:]
            self.size -= 1
            return e
        else:
            return None

    def remove(self, r):
        '''
        '''
        if self.is_empty() is False:
            self.data.remove(r)
            self.size -= 1
        else:
            pass
    
    def first(self):
        '''
        '''
        return self.data[0]
    
    def last(self):
        '''
        '''
        return self.data[-1]

    def is_empty(self):
        '''
        '''
        return self.size == 0