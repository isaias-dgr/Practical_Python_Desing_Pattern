from logger import Logger
from modulo import function
from threading import Thread
# from singleton_object import SingletonObject

# obj1 = SingletonObject()
# obj1.val = "Object value 1"

# print(f"print obj1: {obj1}")

# obj2 = SingletonObject()
# obj2.val = "Object value 2"
# print("------------------------------")
# print(f"print obj1: {obj1}")
# print(f"print obj2: {obj2}")

# log  = Logger('file_log.log')
# print(log)


def test_singleton(value):
    log = Logger('file_log.log')
    log.warn(f"test_singleton {value}")


if __name__ == "__main__":
    try:
        # log.info("ok")
        # function()

        process1 = Thread(target=test_singleton, args=("th1",))
        process2 = Thread(target=test_singleton, args=("th2",))
        process1.start()
        process2.start()

        a = 1 / 0
    except:
        pass
        # log.error("something went wrong")
