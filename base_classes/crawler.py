from abc import ABC, abstractmethod 
from typing import TypeVar, Generic

T = TypeVar('T')

class crawler(ABC):
    '''
        Base class representing an abstract crawler. 
        Every crawler should inherit from this class in order to avoid dependecies
    '''
    def __init__(self):
        pass

    @abstractmethod
    def start(self) -> T:
        '''
            Abstract method inside base class. Once implemented by derivered classes, it is supposed
            to start crawling some data in some endpoint.

            It has to return a 'typed' object (T)
        '''
        pass
    pass