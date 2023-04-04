# Pablo Hernandez Martinez, pablo.hernandez.martinez@udc.es - Marcelo Ferreiro Sánchez, marcelo.fsanchez@udc.es
class Avion():
    '''
    Attributes:
    ----------
    name: str
        Name of the plane.
    flight_class: str
        Type of flight.
    priority: int
        Priority of the flight.
    original_entry_time
        Time at which the plane entered the queue for the first time.
    new_entry_time
        Time at which the plane was relocated to a new queue.
    wait_time
        Amount of time the plane has waited in total.

    Methods:
    ---------
    get_name():
        Returns the name of the plane
    set_name(input_name):
        sets the name of the plane
    get_flight_class():
        returns the class of the flight
    set_flight_class(input_flight_class):
        sets the class of a flight.
    get_priority():
        returns the priority of a flight
    set_priority(input_priority):
        changes the priority of a flight
    get_original_entry_time():
        returns the original entry time of the plane
    set_original_entry_time(input_original_entry_time):
        changes the original entry time of the plane
    get_new_entry_time():
        returns the new entry time of the flight
    set_new_entry_time(input_new_entry_time):
        changes the new entry time of the flight
    get_wait_time():
        returns the wait time of the plane
    set_wait_time(input_wait_time):
        changes the wait time of the plane
    
    '''
    def __init__(self, name, flight_class, priority):
        '''
    This method initializes the attributes based on the arguments given.
        
        Parameters
        ----------
        name: str
            name of the plane
        flight_class: str
            Type of flight.
        priority: int
            Priority of the flight. 
        '''
        self.name = name
        self.flight_class = flight_class
        self.priority = priority
        self.original_entry_time = 0
        self.new_entry_time = 0
        self.wait_time = 0
            
    def get_name(self):
        '''
        Returns the plane name.
        Parameters
        ----------
        Self
        Returns
        ----------
        string
            Name of the plane

        '''
        return self.name
    
    def set_name(self, input_name):
        '''
        Sets the name of the plane
        Patameters
        ----------
        Self
        input_name: Str
            Name to be put 
        Returns
        ----------
        None

        '''
        self.name = input_name
        
    def get_flight_class(self):
        '''
        Returns the flight class
        Parameters
        ----------
        Self
        Returns
        ----------
        Str
            Class of plane

        '''
        return self.flight_class
    
    def set_flight_class(self, input_flight_class):
        '''
        Changes the class of a plane
        Parameters
        -----------
        Self
        input_flight_class: Str
            New class of the flight
        Returns
        -----------
        None 
        '''
        self.flight_class = input_flight_class
        
    def get_priority(self):
        '''
        Returns the priority of the plane

        Parameters
        -----------
        Self
        Returns
        -----------
        Self. priority: int
            Priority of the flight

        '''
        return self.priority
    
    def set_priority(self, input_priority):
        '''
        Changes the priority of a flight
        Parameters
        -----------
        Self
        input_priority: int
            New priority of the plane
        Returns
        -----------
        None
        
        '''
        self.priority = input_priority

    def get_original_entry_time(self):
        '''
        Returns the original entry time of the plane
        Parameters
        ----------
        Self
        Returns
        ----------
        self.original_entry_time: int
            Original entry time of the plane

        '''
        return self.original_entry_time
    
    def set_original_entry_time(self, input_original_entry_time):
        '''
        Changes the original entry time of the flight
        Parameters
        ----------
        Self
        input_original_entry_time: int
            New original entry time
        Returns
        ----------
        None
        '''
        self.original_entry_time = input_original_entry_time
        
    def get_new_entry_time(self):
        '''
        Returns the new entry time
        Parameters
        ----------
        Self
        Returns
        ----------
        self.new_entry_time: int
            new entry time of the flight
        '''
        return self.new_entry_time
    
    def set_new_entry_time(self, input_new_entry_time):
        '''
        Changes the new entry time of the flight
        Parameters
        -------------
        Self
        input_new_entry_time: int
            new new entry time of the plane
        Returns
        ---------------
        None

        '''
        self.new_entry_time = input_new_entry_time
        
    def get_wait_time(self):
        '''
        Returns the wait time of the flight
        Parameters
        -----------
        Self
        Returns
        ------------
        self.wait_time : int
            Wait time of the flight

        '''
        return self.wait_time
    
    def set_wait_time(self, input_wait_time):
        '''
        Changes the wait time
        Parameters
        -----------
        Self
        input_wait_time: int
            new wait time of the plane
        Returns
        -----------
        None
        '''
        self.wait_time = input_wait_time