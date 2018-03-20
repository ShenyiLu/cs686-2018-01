from logger import logger
class stdout_logger(logger):
    
    '''
    Constructors are included in base class
    '''

    """
    log
    Logs the message if log_level is less than or equal to
    the class' threshold. (In this case: print log_level 
    and message to console.)
    """
    def log(self, log_level, message):
        if self.__log_level__ >= log_level:
            print(log_level,": ",message)
        return