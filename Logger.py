import logging

class Logg():
    logging.basicConfig(level=logging.INFO, filename="py_log.log", filemode="w")
    def __init__(self):
        self.logger = logging.getLogger()

    def makeLog(self,text):
        self.logger.info(text)


