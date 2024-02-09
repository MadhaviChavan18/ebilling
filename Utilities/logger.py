
import logging

class Logclass():
    def getclass(self):
        #getLogger() method takes the test case name as input
        logger = logging.getLogger()
        # FileHandler() method takes location and path of log file
        fileHandler = logging.FileHandler("Logs\\logfile123.log")
        # Formatter() method takes care of the log file formatting
        formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")
        fileHandler.setFormatter(formatter)
        # addHandler() method takes fileHandler object as parameter
        logger.addHandler(fileHandler)
        # setting the logger level
        logger.setLevel(logging.DEBUG)
        logger.debug("Debug log")
        logger.info("Information log")
        logger.warning("Warning log")
        logger.error("Error log")
        logger.critical("Critical log")
        return logger


# import  logging
#
# class logclass:
#     def getthelogs(self):
#         logger = logging.getLogger()
#         filehandler = logging.FileHandler("Logs\\logfile.log",mode="w")
#         formatter = logging.Formatter('%(asctime)s: %(modules)s: %(funcName)s: %(message)s',datefmt='%d%m%y %I:%M:%S:%P')
#         filehandler.setFormatter(formatter)
#         logger.addHandler(filehandler)
#         logger.setLevel(logging.INFO)
#         return logger
