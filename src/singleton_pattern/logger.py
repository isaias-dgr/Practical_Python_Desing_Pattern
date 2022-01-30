# from logger_safe import LoggerMeta
from logger_simple import LoggerMeta

class Logger(metaclass=LoggerMeta):

    def __init__(self, file_name):
        self.__file_name = file_name


    def __write_log(self,  level, msg):
        with open(self.__file_name, "a") as log_file:
          log_file.write(f"[{level}], {msg}\n")


    def critical(self, msg):
      self.__write_log("CRITICAL", msg)


    def error(self, msg):
        self.__write_log("ERROR", msg)


    def warn(self, msg):
        self.__write_log("WARN", msg)


    def info(self, msg):
        self.__write_log("INFO", msg)


    def debug(self, msg):
     self.__write_log("DEBUG", msg)

    def __str__(self) -> str:
        return f"Logger in file {self.__file_name} "

