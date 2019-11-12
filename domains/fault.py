class fault:
    """
        Class representing a Fault
    """
    plant: str = ''
    bit: str = ''

    def __init__(self, _plant: str, _bit: str):
        """
        Class init

        Args:
            _plant: Plant name
            _bit: Bit representing the fault
        """
        self.plant = _plant
        self.bit = _bit
        pass
    
    def is_notify_required(self) -> bool:
        pass

    def parse_message(self) -> str:
        """
        Method responsible to perfor some busness rules and define a friendly message based on 'Plan' & 'Bit' informations

        Returns:
            Frindly message
        """
        return ''
    pass