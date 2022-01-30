from logger import Logger

log = Logger("file_log.log")
print(log)

def function():
    log.debug("Other file")
