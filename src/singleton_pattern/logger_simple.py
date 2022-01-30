from threading import Lock

class LoggerMeta(type):

    _instance = {}
    _lock: Lock = Lock()

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instance:
            instance =  super().__call__(*args, **kwargs)
            cls._instance[cls] = instance
        return cls._instance[cls]
