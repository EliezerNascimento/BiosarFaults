from abc import ABC, abstractmethod 

class notifier(ABC):
    '''
        Base class representing an abstract notifier. 
        Every notifier should inherit from this class in order to avoid dependecies
    '''
    def __init__(self):
        pass

    @abstractmethod
    def notify(self, _origin: str, _destination: str, _message: str) -> bool:
        '''
            Abstract method inside base class. Once implemented by derivered classes, it is supposed
            to send specific messages to a destination 

            Args:
               _origin: Message origin
               _destination: Message destination
               _message: Message
        '''
        pass
    pass