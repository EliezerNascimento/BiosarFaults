from abc import ABC, abstractmethod 
from typing import TypeVar, Generic

T = TypeVar('T')

class data_base(ABC):
    '''
        Base class representing an abstract database. 
        Every database class should inherit from this class in order to avoid dependecies
    '''
    def __init__(self):
        pass

    @abstractmethod
    def save(self, _obj: T) -> bool:
        '''
            Abstract method inside base class. Once implemented by derivered classes, it is supposed
            to save some data to a destination database.

            Args:
                _obj: Object to be persisted to a database

            Returns:
                Boolean indicating the operation status ('True' in case o success; otherwise, 'False') 
        '''
        pass
    pass