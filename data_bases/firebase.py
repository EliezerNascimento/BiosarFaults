from base_classes.data_base import data_base
from domains.fault import fault

class firebase(data_base):
    def save(self, _obj: fault) -> bool:
        '''
            It is supposed to save some data to a destination database.

            Args:
                _obj: Object to be persisted to a database

            Returns:
                Boolean indicating the operation status ('True' in case o success; otherwise, 'False') 
        '''
        return False
    pass