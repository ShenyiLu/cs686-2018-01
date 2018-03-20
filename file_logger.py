from logger import logger
class file_logger(logger):
    '''
    Constructors are included in base class
    '''

    """
    log
    Logs the message if log_level is less than or equal to
    the class' threshold. (In this case: print log_level 
    and message to a given file.)
    """
    def log(self, log_level, message, filename='file_log.txt'):
        if self.__log_level__ >= log_level:
            my_file = open(filename, "w+")
            my_file.write((str(log_level) + ": " + message))
            my_file.close()
        return

