import logging

class Logg():
    def __init__(self, name):
        self.logger = logging.getLogger(name)
        logging.basicConfig(level=logging.INFO, filename=f'{name}.log', filemode="w")
    #@staticmethod
    def makeLog(self,text):
        self.logger.info(msg=text)


