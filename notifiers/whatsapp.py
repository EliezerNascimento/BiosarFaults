from base_classes.notifier import notifier

class whatsapp(notifier):
    def notify(self, _origin: str, _destination: str, _message: str) -> bool:
        '''
            Abstract method inside base class. Once implemented by derivered classes, it is supposed
            to send specific messages to a destination 

            Args:
               _origin: Message origin
               _destination: Message destination
               _message: Message
        '''
        return False
    pass